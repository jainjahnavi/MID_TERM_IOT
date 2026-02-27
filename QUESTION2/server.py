#multi chat system
import threading
import socket

#from TCP.Client import client

#host="0.0.0.0"
#port=5000

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(("localhost",5000))
server.listen(5)

clients=[]
usernames=[]

print("server started")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
#jo bhi client aayegaa voh jb tk chat khtm nhii hotii tb tk communicate kregaa
 while True:
     try:
         message=client.recv(1024)
         broadcast(message)
     except:
         index=clients.index(client)
         clients.remove(client)
         username=usernames[index]
         usernames.remove(username)
         broadcast(f"{username} left the chat".encode())
         break



def rec_connection(): #receive connecton
    while True:
        client,addr=server.accept()
        print("connected to: ",addr)
        client.send("username".encode()) #username bhejoo
        username=client.recv(1024).decode()

        usernames.append(username)
        clients.append(client)

        print(f"{username} has joined the chat")
        broadcast(f"{username} has joined the chat".encode())
        thread=threading.Thread(target=handle_client,args=(client,))
        thread.start()
rec_connection()