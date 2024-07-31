import threading
import socket
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

# Server setup
host = '127.0.0.1'
port = 59000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

clients = []
aliases = []

# Function to broadcast messages to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle client communication
def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            alias = aliases[index]
            broadcast(f'{alias} has left the chat room!'.encode('utf-8'))
            aliases.remove(alias)
            break

# Function to receive client connections
def receive():
    server.listen()
    while True:
        client, address = server.accept()
        log_message(f'Connection established with {str(address)}')
        client.send('alias>'.encode('utf-8'))
        alias = client.recv(1024).decode('utf-8')
        aliases.append(alias)
        clients.append(client)
        log_message(f'The alias of this client is {alias}')
        broadcast(f'{alias} has connected to the chat room'.encode('utf-8'))
        client.send('You are now connected!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

# Function to start the server
def start_server():
    threading.Thread(target=receive).start()
    log_message('Server is running and listening...')

# Function to stop the server
def stop_server():
    for client in clients:
        client.close()
    server.close()
    log_message('Server has been stopped.')
    app.quit()

# Function to log messages in the GUI
def log_message(message):
    log_window.config(state=tk.NORMAL)
    log_window.insert(tk.END, message + '\n')
    log_window.config(state=tk.DISABLED)

# Client setup
def start_client():
    alias = simpledialog.askstring("Alias", "Choose an alias")
    if alias:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))

        def client_receive():
            while True:
                try:
                    message = client.recv(1024).decode('utf-8')
                    if message == "alias>":
                        client.send(alias.encode('utf-8'))
                    else:
                        print(message)
                except:
                    print('Error!')
                    client.close()
                    break            

        def client_send():
            while True:
                message = f'{alias}: {input("")}'
                client.send(message.encode('utf-8'))

        receive_thread = threading.Thread(target=client_receive)
        receive_thread.start()

        send_thread = threading.Thread(target=client_send)
        send_thread.start()

# GUI setup
app = tk.Tk()
app.title("Chat Server and Client")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

log_window = scrolledtext.ScrolledText(frame, state='disabled', width=50, height=20)
log_window.pack()

start_server_button = tk.Button(frame, text="Start Server", command=start_server)
start_server_button.pack(side=tk.LEFT, padx=5)

stop_server_button = tk.Button(frame, text="Stop Server", command=stop_server)
stop_server_button.pack(side=tk.LEFT, padx=5)

start_client_button = tk.Button(frame, text="Start Client", command=start_client)
start_client_button.pack(side=tk.LEFT, padx=5)

# Run the GUI
app.protocol("WM_DELETE_WINDOW", stop_server)
app.mainloop()
