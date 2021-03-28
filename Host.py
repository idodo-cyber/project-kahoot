import socket
import threading
from Client_class import Client
SIP = "127.0.0.1"
IP = "0.0.0.0"
CLINET_ARR = []
SPORT = 55368
MPORT = 53476
lock = threading.Lock()
ANS_WORTH = 100
ANS_TIME = 60000
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

    k.send(build_ans("bye").encode())
    k.close()#closes connection with server
    handle_quiz()#handles the quiz






def get_pin():#recieves game pin from server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    s.send((str(len("hello"))+"_"+"hello").encode())
    print(all_mesage(s))
    return s

def connect_client(c,addr):#connects client and sets him up with the clients nickname
    name = all_mesage(c)
    while  not name_in(name):
        c.send(build_ans("taken").encode())#checks if the nickname is taken
        name = all_mesage(c)
    cli = Client(name,c)
    lock.acquire()
    CLINET_ARR.append(cli)
    lock.release()
    print(name)
    c.send(build_ans("good").encode())

def handle_quiz():
    with open("demo_quiz") as file:
        first_lines = "".join([file.readline() for _ in range(5)]).split("\n")
        while not first_lines == [""]:
            print(first_lines)
            for i in first_lines:
                if "_T" in i:
                    ans = i.split("_")
                    arr = []
                    for cli in CLINET_ARR:
                        thread = threading.Thread(target=handle_ans,args=(ans[1], cli))  # creates new thread for client
                        thread.start()
                        arr.append(thread)
                    for thr in arr:
                        thr.join()#waits until all clients are finished
                    CLINET_ARR.sort(key = lambda x:x.value,reverse=True)#sorts the clients based on their value
                    for i in CLINET_ARR:
                        i.socket.send(build_ans(str(i.value) + "_" + str(i.added_value) + "_"+str(CLINET_ARR.index(i)+1)).encode())
                        #sends the value,added value and place of client to client to the client

            first_lines = "".join([file.readline() for _ in range(5)]).split("\n")
        for i in CLINET_ARR:
            i.end_client()
        CLINET_ARR.clear()



def name_in(name):#checks if the given client object has a name similer to a name prevoiusly taken
    for i in CLINET_ARR:
        if name == i.Get_name():
            return False
    return True
def all_mesage(sock):#recievs all of the message based on the message length given at the begining of the messsage
    lent = sock.recv(1).decode()
    while "_" not in lent:
        lent += sock.recv(1).decode()
    lent = int(lent[:-1])#recives the message length
    ans = sock.recv(lent).decode()
    while not len(ans) == lent:
        ans += sock.recv(lent)
    return ans#recieves the message

def build_ans(ans):
    return str(len(ans))+"_"+ans

def handle_ans(true,cli):#handles the given ans and adds points accordingly
    cli.strt_classes()#sends start message to client
    ans,time = cli.recv_ans()#recieves answer and time it tokk to answer from client
    if ans == true:#if answer is correct adds the corresponding value
        val = 1-(int(time)/ANS_TIME/2)
        val = int(val*ANS_WORTH)
    else:
        val = 0
    cli.add_value(val)
    cli.Set_added_value(val)



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