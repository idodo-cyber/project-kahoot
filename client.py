import socket
import datetime
SIP = "10.100.102.12"
SPORT = 55368
MPORT = 53476

def client():#main loop of the client
   ip = get_addr()
   while  ip == None:
       ip = get_addr()
   s = cnct_client(ip)
   ans = ""
   while not ans == "STP":
       ans = all_mesage(s)
       if ans == "STRT":
            answer = build_ans()
            s.send(answer.encode())
       point = all_mesage(s).split("_")
       print("you have " + point[0] + " you gained "+point[1] + "and you are at place" + point[2])




def get_addr():#gets the ip addr based on game pin
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    print("what is the passwrd")
    ans = input()
    s.send("please".encode())
    s.send(ans.encode())#unite both lines ointo a single message and build func at server file to break the message down
    addr = s.recv(1024).decode()
    return addr

def build_ans():
    start_time = datetime.datetime.now()
    ans = input()#this will change to choose based on button
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    exe = int(execution_time)
    ans = str(len(ans + "_" + str(exe))) + "_" + ans + "_" + str(exe)#builds the answer based on protocol len_ans_time
    return ans



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

def all_mesage(sock):#recievs all of the message based on the message length given at the begining of the messsage
    lent = sock.recv(1).decode()
    while "_" not in lent:
        lent += sock.recv(1).decode()
    print(lent)
    lent = int(lent[:-1])#recives the message length
    ans = sock.recv(lent).decode()
    print(ans)
    while not len(ans) == lent:
        ans += sock.recv(lent)
    return ans#recieves the message

handle()