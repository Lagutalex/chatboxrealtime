import socket
import sys
import time



s = socket.socket()
host = socket.gethostname()
print(" Server bu hostta başlıcak: ", host)
port = 8080
s.bind((host,port))
print("")
print(" Sunucu porta ve hosta bağlanıyor")
print("")
print("Sunucu gelenleri bekliyor")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, " Servera bağlandı ve şuan online")
print("")
while 1:
            message = input(str(">> "))
            message = message.encode()
            conn.send(message)
            print("message has been sent...")
            print("")
            incoming_message = conn.recv(1024)
            incoming_message = incoming_message.decode()
            print(" Client : ", incoming_message)
            print("")
