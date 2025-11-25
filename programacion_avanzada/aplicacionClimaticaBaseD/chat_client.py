import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

# --- Configuración del Cliente ---
HOST = '127.0.0.1'
PORT = 65432

class ChatClient:
    def __init__(self, master):
        self.master = master
        master.title("Cliente de Chat de Soporte")
        master.geometry("400x500")

        # --- Ventana para pedir el apodo (Nickname) ---
        self.nickname = simpledialog.askstring("Apodo", "Por favor, introduce tu apodo:", parent=master)
        if not self.nickname:
            master.destroy()
            return
            return
        
        master.title(f"Soporte Técnico - {self.nickname}")

        # --- Creación de Widgets de la GUI ---
        self.chat_box = scrolledtext.ScrolledText(master, state='disabled', wrap=tk.WORD)
        self.chat_box.pack(padx=10, pady=10, expand=True, fill='both')
        
        self.msg_entry = tk.Entry(master, width=50)
        self.msg_entry.pack(padx=10, pady=5, side='left', expand=True, fill='x')
        self.msg_entry.bind("<Return>", self.send_message)

        self.send_button = tk.Button(master, text="Enviar", command=self.send_message)
        self.send_button.pack(padx=10, pady=5, side='right')
        
        # --- Conexión al servidor ---
        self.client_socket = None
        self.connect_to_server()

        # --- Manejar el cierre de la ventana ---
        master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def connect_to_server(self):
        """
        Intenta conectar con el servidor de chat.
        """
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((HOST, PORT))
            self.client_socket.send(self.nickname.encode('utf-8'))
            
            # --- Iniciar hilo para recibir mensajes ---
            receive_thread = threading.Thread(target=self.receive_messages)
            receive_thread.daemon = True # El hilo muere si el programa principal cierra
            receive_thread.start()

        except ConnectionRefusedError:
            # --- Manejo de error si el servidor no está activo ---
            messagebox.showerror("Error de Conexión", "No se pudo conectar al servidor de soporte. Asegúrese de que el servidor esté en ejecución.")
            self.master.destroy()

    def receive_messages(self):
        """
        Recibe mensajes del servidor y los muestra en la caja de chat.
        """
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.display_message(message)
                else:
                    # --- Si no hay mensaje, el servidor se ha cerrado ---
                    self.display_message("SOPORTE: Se ha perdido la conexión con el servidor.\n")
                    break
            except:
                # --- Manejo de errores de conexión ---
                self.display_message("SOPORTE: Ocurrió un error en la conexión.\n")
                break
        
        # --- Desactivar controles cuando se pierde la conexión ---
        self.msg_entry.config(state='disabled')
        self.send_button.config(state='disabled')

    def send_message(self, event=None):
        """
        Envía el mensaje del cuadro de entrada al servidor.
        """
        message = self.msg_entry.get()
        if message:
            full_message = f"{self.nickname}: {message}\n"
            self.client_socket.send(full_message.encode('utf-8'))
            self.display_message(full_message) # Muestra el propio mensaje
            self.msg_entry.delete(0, 'end')

    def display_message(self, message):
        """
        Muestra un mensaje en el chat_box de forma segura entre hilos.
        """
        self.chat_box.config(state='normal')
        self.chat_box.insert('end', message)
        self.chat_box.config(state='disabled')
        self.chat_box.see('end')

    def on_closing(self):
        """
        Se ejecuta al cerrar la ventana para notificar al servidor.
        """
        if self.client_socket:
            # --- No se envía mensaje de salida, el servidor lo detecta ---
            self.client_socket.close()
        self.master.destroy()

# --- Punto de entrada para ejecutar el cliente de forma independiente ---
if __name__ == "__main__":
    root = tk.Tk()
    client = ChatClient(root)
    root.mainloop()
