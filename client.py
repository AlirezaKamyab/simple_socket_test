import socket
import threading

PORT = 5050
IP = "192.168.137.1"
ADDR = (IP, PORT)
FORMAT = "utf-8"
EOC = "END"

client = socket.socket()
client.connect(ADDR)

def RecieveMessage():
    try:
        while True:
            msg = client.recv(2048).decode(FORMAT)
            if msg:
                print(msg)
    except:
        pass

def send_messages():
    while True:
        msg = input("Your message to the server: ")
        client.send(msg.encode(FORMAT))

        if msg == EOC: break

    client.close()

def main():
    recvThread = threading.Thread(target=RecieveMessage, args=())
    recvThread.start()

    sendThread = threading.Thread(target=send_messages, args=())
    sendThread.start()

if __name__ == "__main__": main()

