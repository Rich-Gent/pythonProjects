import socket
import threading

#function for sending messages
def send_message():
    while True:
        #send message to server
        msg = input(name)
        if msg == "quit":
            break
        else:
            client.send((name+msg).encode("utf-8"))

#functgion for recieving messages
def receive_message():
    #print message from server
    while True:    
        print(client.recv(1024).decode("utf-8"))
#set threding
if __name__ =="__main__":
    name = input("Please input your username: ")
    name += ": "
    #set up a client using the internet and sock stream for a constant stream of data
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #connect client to server and port
    client.connect(("localhost", 9999))
    t1 = threading.Thread(target=send_message)
    t2 = threading.Thread(target=receive_message)
 
    t1.start()
    t2.start()
 
    t1.join()
 
    print("Done!")
    client.close()

