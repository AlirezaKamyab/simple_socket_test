#!/usr/bin/env python3

import socket
import threading

PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = "utf-8"
EOC = "END"

client_list = []
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main():
    server.bind(ADDR)
    server.listen()

    while True:
        print(f"[Waiting for clients] {ADDR}")
        conn, addr = server.accept()

        client_list.append({"addr":addr, "conn": conn})
        thread = threading.Thread(target=client, args=(conn, addr))
        thread.start()


def client(conn, addr):
    print(f"[{addr}] client is connected")
    connection = True  
    try:
        while connection:
            msg = conn.recv(2048).decode(FORMAT)
            if msg:
                threading.Thread(target=send_to_all, args=(msg,addr)).start()
                if msg == EOC:
                    connection = False
    except:
        connection = False
        conn.close()

    conn.close()

    for c in client_list:
        if c["addr"] == addr:
            client_list.remove(c)
            

def send_to_all(msg, fromAddress):
    try:
        for c in client_list:
            if c['addr'] == fromAddress: continue
            c["conn"].send(msg.encode(FORMAT))
    except:
        pass

if __name__ == "__main__": main()