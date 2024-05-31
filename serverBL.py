import socket
from threading import Thread
import UI as ui

server = None
client = None
check = False


# Steps
# 1. Device Manager -> Realtek Bluetooth Adapter
# 2. Right Click -> Properties -> Advanced -> Address
# 3. Turn on Bluetooth on both devices and make server device visible

def threaded(mac):
    Thread(target=startsv, args=(mac,)).start()

def returnCheck():
    return check

def resetChange():
    change = False
def startsv(mac):
    global server
    global client, check
    server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)  # RFCOMM specific protocol
    server.bind((mac, 4))  # MAC Address and Channel 4 bc:54:2f:8b:78:55
    server.listen(1)  # 1 adet cihaz
    check = True
    print("Waiting for connection...")

    try:
        client, addr = server.accept()
        print(f"Bağlantı kabul edildi: {addr}")

        # Burada client ile iletişim kurabilirsiniz, örneğin:
        # client.sendall(b"Merhaba, bu sunucu!")
        # client.close()

    except socket.error as e:
        print(f"Bir hata oluştu: {e}")
        # server.close()
        print("HATASONRASI")

    print(f"Accepted connection from {addr}")

    try:
        while True:
            data = client.recv(1024)
            if not data:
                break
            came = data.decode('utf-8')
            ui.txtController(1)
            ui.setTxt(came)
            ui.txtController(0)
            print(f"Received: {came}")

            #message = ui.getMessage()
            #client.send(message.encode('utf-8'))
    except OSError:
        pass

    print("Disconnected")
    stop()

def sendMessage(message):
    client.send(message.encode('utf-8'))
def stop():
    global client
    global server

    server.close()
    return 0
