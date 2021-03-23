import socket
import threading
from Client_class import Client
SIP = "10.100.102.114"
IP = "0.0.0.0"
CLINET_ARR = []
SPORT = 55368
MPORT = 53476
lock = threading.Lock()
def host():#creates the host by getting the pin an connecting the cllinets
    k = get_pin()#gets pin
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, MPORT))#creates ne server
    var = 0
    arr = []#creates an array for the threads for each client
    while var <2:#two clients needs to change to infinit aith timeouts
        s.listen()
        c, addr = s.accept()
        print("here")
        thread = threading.Thread(target=connect_client, args=(c, addr))#creates new thread for client
        thread.start()
        arr.append(thread)
        var += 1
    for i in arr:
        i.join()#waits until all clients are connected an set

    k.send("bye".encode())
    k.close()#closes connection with server
    for i in CLINET_ARR:
        print(i.To_string())



def get_pin():#recieves game pin from server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    s.send("hello".encode())
    print(s.recv(1024).decode())
    return s

def connect_client(c,addr):#connects client and sets him up with the clients nickname
    name = (c.recv(1024)).decode()
    while  not name_in(name):
        c.send("taken".encode())#checks if the nickname is taken
        name = (c.recv(1024)).decode()
    cli = Client(name,c)
    lock.acquire()
    CLINET_ARR.append(cli)
    lock.release()
    print(name)
    c.send("good".encode())




def name_in(name):#checks if the given client object has a name similer to a name prevoiusly taken
    for i in CLINET_ARR:
        if name == i.Get_name():
            return False
    return True




def main():#main loop of
   while True:
        print("what am i")
        ans = input()
        if ans == "host":
            host()
        else:
            print("please enter appropriate ans")

if __name__ == '__main__':
    main()