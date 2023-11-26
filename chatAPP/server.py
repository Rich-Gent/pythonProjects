import socket
import threading

#function for sending messages
def send_message():
    while True:
        #send message back to all clients
        msg = input(name)
        if msg == 'quit':
            client.close()
            break
        else:
            client.send((name + msg).encode('utf-8'))

#function for recieving messages
def receive_message():
    #for each client print out message using 1024 bytes
    while True:
        print(client.recv(1024).decode('utf-8'))



if __name__ =="__main__":
    name = input("Please input your username: ")
    name+=": "
    #set up a server using the internet and sock stream for a constant stream of data
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind server to port
    server.bind(("localhost", 9999))

    #server will listen to a specific port
    server.listen()
    client, addr = server.accept()
    
    t1 = threading.Thread(target=send_message)
    t2 = threading.Thread(target=receive_message)
 
    t1.start()
    t2.start()
 
    t1.join()
 
    print("Done!")
    server.close()
