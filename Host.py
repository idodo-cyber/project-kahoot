import socket
import threading
from Client_class import Client
import tkinter as tk
from functools import partial
SIP = "127.0.0.1"
IP = "0.0.0.0"
CLINET_ARR = []
SPORT = 55368
MPORT = 53476
lock = threading.Lock()
ANS_WORTH = 100
ANS_TIME = 60000
CNCT = 0
PROG = 0
QUESTNUM = 5

def set():
    ROOT = tk.Tk()
    # specify size of window.
    ROOT.geometry("400x400")

    # Create text widget and specify size.
    return ROOT
def progress():
    global PROG
    PROG =1


def opening(root,pin):
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="wating for players....")
    title.config(font=("Ariel", 18))
    title.grid(row=0, column=0, sticky="NW")
    title = tk.Label(f, text="the pin is:")
    title.config(font=("Ariel", 18))
    title.grid(row=1,column=0,sticky="NW")
    title = tk.Label(f, text=pin)
    title.config(font=("Ariel", 18))
    title.grid(row=2, column=0, sticky="NW")
    title = tk.Label(f, text="people who have connected are:")
    title.config(font=("Ariel", 18))
    title.grid(row=3, column=0, sticky="NW")
    return f

def question(root, num,question,ans):
        f = tk.Frame(root)
        f.place(relx=0, rely=0)
        title = tk.Label(f, text="questin: " + str(num) + "/" + "3")
        title.config(font=("Ariel", 18))
        title.grid(row=0, column=0, sticky="NW")
        title = tk.Label(f, text=question)
        title.config(font=("Ariel", 18))
        title.grid(row=1, column=0, sticky="NW")
        title = tk.Label(f, text="A." + ans[0])
        title.config(font=("Ariel", 18))
        title.grid(row=2, column=0, sticky="NW")
        title = tk.Label(f, text="B."+ans[1])
        title.config(font=("Ariel", 18))
        title.grid(row=3, column=0, sticky="NW")
        title = tk.Label(f, text="C."+ans[2])
        title.config(font=("Ariel", 18))
        title.grid(row=4, column=0, sticky="NW")
        title = tk.Label(f, text="D."+ans[3])
        title.config(font=("Ariel", 18))
        title.grid(row=5, column=0, sticky="NW")
        return f


def answer(root,  ans):
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="THE ANSWER IS: " )
    title.config(font=("Ariel", 18))
    title.grid(row=1, column=0, sticky="NW")
    title = tk.Label(f, text=ans)
    title.config(font=("Ariel", 18))
    title.grid(row=2, column=0, sticky="NW")
    title = tk.Label(f, text="frst: " + CLINET_ARR[0].name)
    title.config(font=("Ariel", 18))
    title.grid(row=3, column=0, sticky="NW")
    #title = tk.Label(f, text="secnd" + CLINET_ARR[1].name)
    #title.config(font=("Ariel", 18))
    #title.grid(row=0, column=3, sticky="NW")
    #title = tk.Label(f, text="thrd" + CLINET_ARR[2].name)
   # title.config(font=("Ariel", 18))
   # title.grid(row=0, column=4, sticky="NW")
    B = tk.Button(f, text="continue", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=4, column=0, sticky="NW")


    return f


def opening2(root,pin):
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="wating for players....")
    title.config(font=("Ariel", 18))
    title.grid(row=0, column=0, sticky="NW")
    title = tk.Label(f, text="the pin is:")
    title.config(font=("Ariel", 18))
    title.grid(row=1, column=0, sticky="NW")
    title = tk.Label(f, text=pin)
    title.config(font=("Ariel", 18))
    title.grid(row=2, column=0, sticky="NW")
    title = tk.Label(f, text="people who have connected are:")
    title.config(font=("Ariel", 18))
    title.grid(row=3, column=0, sticky="NW")
    n = 4
    for i in CLINET_ARR:
        title = tk.Label(f, text=i.name)
        title.config(font=("Ariel", 18))
        title.grid(row=n, column=0, sticky="NW")
        n = n+1

    if n>=7:
        B = tk.Button(f, text="continue",command = progress)
        B.config(font=("Ariel", 18))
        B.grid(row=n+1, column=0, sticky="NW")
    # Insert The Fact.
    return f




def all_children(window):
    _list = window.winfo_children()

    for item in _list:
        if item.winfo_children():
            _list.extend(item.winfo_children())

    return _list



def reset(frm):
    frm.destroy()
def host(root):#creates the host by getting the pin an connecting the cllinets
    global CRNT_FRM
    global PROG
    k,pin = get_pin()#gets pin
    print(pin)
    CRNT_FRM = opening(root,pin)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP, MPORT))#creates ne server
    var = 0
    arr = []#creates an array for the threads for each client
    while var <3:#two clients needs to change to infinit aith timeouts
        s.listen()
        c, addr = s.accept()
        thread = threading.Thread(target=connect_client, args=(c, root,pin))#creates new thread for client
        thread.start()
        arr.append(thread)
        var += 1
    for i in arr:
        i.join()  # waits until all clients are connected an set
    k.send(build_ans("bye").encode())
    k.close()  # closes connection with server
    while True:
        if PROG == 1:
            PROG = 0
            handle_quiz(root)
            break





def get_pin():#recieves game pin from server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    s.send((str(len("hello"))+"_"+"hello").encode())
    msg = all_mesage(s)
    return s,msg

def connect_client(c,root,pin):#connects client and sets him up with the clients nickname
    global CRNT_FRM
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
    lock.acquire()
    reset(CRNT_FRM)
    CRNT_FRM = opening2(root,pin)
    lock.release()
def split_lines(frst):
    arr = []
    l = 0
    for i in frst:
        var = i.split("_")
        arr.append(var[0])
        l +=1
    return arr


def handle_quiz(root):
    global  CRNT_FRM
    global PROG
    with open("demo_quiz") as file:
        first_lines = "".join([file.readline() for _ in range(5)]).split("\n")
        num = 1
        quest = first_lines[0]
        arr1 = split_lines(first_lines[1:])
        reset(CRNT_FRM)
        CRNT_FRM = question(root, num, quest, arr1)
        print(first_lines)
        while not first_lines == [""]:
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

            reset(CRNT_FRM)
            CRNT_FRM = answer(root,ans[1])
            while True:
                if PROG == 1:
                    PROG = 0
                    break
            first_lines = "".join([file.readline() for _ in range(5)]).split("\n")
            if not first_lines == [""]:
                num +=1
                quest = first_lines[0]
                arr1 = split_lines(first_lines[1:])
                reset(CRNT_FRM)
                CRNT_FRM = question(root, num, quest, arr1)
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






if __name__ == '__main__':
    root = set()
    thread = threading.Thread(target=host,args = (root,))  # creates new thread for client
    thread.start()
    tk.mainloop()



