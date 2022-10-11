# Backdoor-Client-Server-Socket-Python
Simple backdoor using lib python's socket

YouTube Video: https://youtu.be/pE5qPvMZ-DM

# lib
- `from socket import *` # for connection
- `import subprocess` # for cmd command

# Server
- `sock = socket(AF_INET, SOCK_STREAM)` # set TCP socket
- `port = 12345` # port of server
- `sock.bind(('', port)) && sock.listen(1)` # set server
- `conn, addr = sock.accept()` # conn = connection && addr = (client)address
- `conn.send(command.encode())` # send in array bytes
- `conn.recv(1024).decode("utf-8")` #receive and convert in string

# Client
- `CMD = subprocess.Popen(command, ...)` # set subprocess for send CMD command

# Guides
|Guides|Links|
|--|--|
|Establish A Connection|[Link](https://www.inforge.net/forum/threads/1-come-creare-una-backdoor-in-python-stabilire-una-connessione.603065/)|
|Steal Files|[Link](https://www.inforge.net/forum/threads/2-come-creare-una-backdoor-in-python-rubare-i-file.603756/)|
