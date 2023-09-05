from vidstream import AudioSender
from vidstream import AudioReceiver
import threading, socket

ip = socket.gethostbyname(socket.gethostname())

print("Your Ip address is: ", ip)

client = input("Receiver IP: ")
client_port = 5060

receiver = AudioReceiver(ip, 5060)
receive_thread = threading.Thread(target=receiver.start_server)

sender = AudioSender(client, int(client_port))
send_thread = threading.Thread(target=sender.start_stream)

receive_thread.start()
send_thread.start()