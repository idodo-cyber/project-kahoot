import socket
SIP = "10.100.102.12"
SPORT = 55368
MPORT = 53476

def client():#main loop of the client
   ip = get_addr()
   while  ip == None:
       ip = get_addr()
   s = cnct_client(ip)
   while True:
       ans = input()
       if ans == "bye":
           s.close()
           break


def get_addr():#gets the ip addr based on game pin
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    print("what is the passwrd")
    ans = input()
    s.send("please".encode())
    s.send(ans.encode())#unite both lines ointo a single message and build func at server file to break the message down
    addr = s.recv(1024).decode()
    return addr


def cnct_client(ip):#connects client to host based on the ip gotten from server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((ip, MPORT))
    print("what is your nickname")
    name = input()
    s.send(name.encode())  # sends nicname to host
    ans = s.recv(1024).decode()
    while ans == "taken":
        print("the name is taken enter new name")
        name = input()
        s.send(name.encode())  # sends nicname to host
        ans = s.recv(1024).decode()

    return s

def handle():
   while True:
        print("what am i")
        ans = input()
        if ans == "clinet":
            client()
        else:
            print("please enter appropriate ans")

handle()
