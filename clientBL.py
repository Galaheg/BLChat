import socket
from threading import Thread

def threaded(mac):
    Thread(target=startsv, args=(mac,)).start()
def startsv(mac):
    global client
    client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    client.connect(("bc:54:2f:8b:78:55", 4)) #buraya baglandiginiz cihazin BL mac adresi lazim

    print(f"Connected!")

    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            print(f"Received: {data.decode('utf-8')}")

    except OSError:
        pass

def sendMessage(message):
    client.send(message.encode('utf-8'))

def stop():

    print("Disconnected")

    client.close()