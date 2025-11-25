import socket
import threading

# --- Configuración del Servidor ---
HOST = '127.0.0.1'  # localhost
PORT = 65432

# --- Listas para clientes y sus apodos ---
clients = []
nicknames = []

# --- Función para transmitir mensajes a todos los clientes conectados ---
def broadcast(message, _client=None):
    """
    Envía un mensaje a todos los clientes, opcionalmente excluyendo a uno.
    """
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                # Si hay un error, el cliente probablemente se desconectó. Se eliminará en 'handle_client'.
                pass

# --- Función para manejar la conexión de un cliente individual ---
def handle_client(client):
    """
    Gestiona la conexión de un cliente: recibe su apodo, y luego sus mensajes.
    """
    nickname = None
    try:
        # --- Solicitar y almacenar el apodo ---
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)
        
        # --- Mensaje de bienvenida y notificación de conexión ---
        print(f"✅ '{nickname}' se ha conectado.")
        broadcast(f"SOPORTE: ¡'{nickname}' se ha unido al chat!\n".encode('utf-8'))
        client.send("SOPORTE: ¡Conectado al servidor de soporte!\n".encode('utf-8'))

        # --- Bucle para recibir y retransmitir mensajes ---
        while True:
            message = client.recv(1024)
            if not message:
                break
            broadcast(message, client)

    except:
        # El bloque finally se encargará de la limpieza
        pass
    finally:
        # --- Manejo de errores y desconexión ---
        if client in clients:
            index = clients.index(client)
            clients.remove(client)
            if nickname:
                nickname_to_remove = nicknames.pop(index)
                broadcast(f"❌ '{nickname_to_remove}' ha abandonado el chat.\n".encode('utf-8'))
                print(f"'{nickname_to_remove}' se ha desconectado.")
        client.close()

# --- Función principal para iniciar el servidor ---
def start_server():
    """
    Inicia el servidor, lo pone en modo de escucha y acepta nuevas conexiones.
    """
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Permite reutilizar la dirección para evitar errores al reiniciar rápidamente
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        server.bind((HOST, PORT))
    except OSError as e:
        print(f"!!! ERROR AL INICIAR EL SERVIDOR: {e}")
        print(f"--- Es posible que el puerto {PORT} ya esté en uso por otro proceso.")
        return

    server.listen()
    
    print(f"✅ Servidor de chat escuchando en {HOST}:{PORT}")
    
    while True:
        try:
            client, address = server.accept()
            print(f"🔌 Conexión aceptada desde {str(address)}")
            
            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
        except KeyboardInterrupt:
            print("\n shutting down server...")
            server.close()
            break

# --- Punto de entrada del script ---
if __name__ == "__main__":
    start_server()