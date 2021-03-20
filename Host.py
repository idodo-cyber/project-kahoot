import socket
import threading
SIP = "10.100.102.114"
IP = "0.0.0.0"
NAME_SOCK = {}
NAME_VALUE = {}
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
    print(NAME_VALUE)
    print(NAME_SOCK)



def get_pin():#recieves game pin from server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    s.send("hello".encode())
    print(s.recv(1024).decode())
    return s

def connect_client(c,addr):#connects client and sets him up with the clients nickname
    name = (c.recv(1024)).decode()
    if name in NAME_SOCK:
        c.send("taken".encode())#checks if the nickname is taken
    else:
        lock.acquire()
        NAME_SOCK[name] = c
        NAME_VALUE[name] = 0
        lock.release()
        print(name)
        c.send("good".encode())






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