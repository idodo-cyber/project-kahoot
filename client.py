import socket
import datetime
import tkinter as tk
import threading
import Kahoot
SIP = "127.0.0.1"
SPORT = 55368
MPORT = 53476
PROG = 0
CHOICE = 0
IP = "0.0.0.0"
CLINET_ARR = []
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
    return ROOT
def openinggg(root,pin):
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
def Host_button():
   global STAT
   STAT = 1

def client_button():
   global STAT
   STAT = 2



def resety(r):
    def all_children(window):
        _list = window.winfo_children()

        for item in _list:
            if item.winfo_children():
                _list.extend(item.winfo_children())

        return _list

    widget_list = all_children(r)
    for item in widget_list:
        try:
            item.grid_forget()
        except AttributeError:
            pass




def screen(root):
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="welcome to Iquiz!!!!!")
    title.config(font=("Ariel", 18))
    title.grid(row=0, column=0, sticky="NW")
    title = tk.Label(f, text="please select your role")
    title.config(font=("Ariel", 18))
    title.grid(row=1,column=0,sticky="NW")
    B = tk.Button(f, text="Host",  command=lambda :Host_button())
    B.config(font=("Ariel", 18))
    B.grid(row=4, column=0, sticky="NW")
    B = tk.Button(f, text="player", command=client_button)
    B.config(font=("Ariel", 18))
    B.grid(row=5, column=0, sticky="NW")
    return f




def progress():
    global PROG
    PROG =1

def reset(frm):
    frm.destroy()

def send_choice():
    global CHOICE

def opening1(root):
    global PROG
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    n=0
    title = tk.Label(f, text="please enter correct pin")
    title.config(font=("Ariel", 18))
    title.grid(row=n,column=0,sticky="NW")
    entry = tk.Entry(f)
    entry.grid(row=n+1,column=0,sticky="NW")
    B = tk.Button(f, text="continue", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=n+2, column=0, sticky="NW")
    while True:
        if PROG == 1:
            PROG = 0
            ans = entry.get()
            break
    return f,ans



def opening2(root):
    global PROG
    global CRNT_FRM
    reset(CRNT_FRM)
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="please enter apropriate pin")
    title.config(font=("Ariel", 18))
    n=0
    title.grid(row=n, column=0, sticky="NW")
    title = tk.Label(f, text="the pin is:")
    title.config(font=("Ariel", 18))
    title.grid(row=n+1,column=0,sticky="NW")
    entry = tk.Entry(f)
    entry.grid(row=n+2,column=0,sticky="NW")
    B = tk.Button(f, text="continue", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=n+3, column=0, sticky="NW")
    while True:
        if PROG == 1:
            PROG = 0
            ans = entry.get()
            break
    return f,ans

def wating(root):
    global PROG
    global CRNT_FRM
    reset(CRNT_FRM)
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="please wait for other players")
    title.config(font=("Ariel", 18))
    title.grid(row=0, column=0, sticky="NW")
    CRNT_FRM = f

def get_name(root):
    global PROG
    global CRNT_FRM
    reset(CRNT_FRM)
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="what is your name?:")
    title.config(font=("Ariel", 18))
    title.grid(row=1,column=0,sticky="NW")
    entry = tk.Entry(f)
    entry.grid(row=2,column=0,sticky="NW")
    B = tk.Button(f, text="continue", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=4, column=0, sticky="NW")
    while True:
        if PROG == 1:
            PROG = 0
            ans = entry.get()
            break
    return f,ans

def get_name2(root):
    global PROG
    global CRNT_FRM
    reset(CRNT_FRM)
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="the name u entered is taken,please enter a new name")
    title.config(font=("Ariel", 18))
    title.grid(row=0, column=0, sticky="NW")
    title = tk.Label(f, text="what is your name?:")
    title.config(font=("Ariel", 18))
    title.grid(row=1,column=0,sticky="NW")
    entry = tk.Entry(f)
    entry.grid(row=2,column=0,sticky="NW")
    B = tk.Button(f, text="continue", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=4, column=0, sticky="NW")
    while True:
        if PROG == 1:
            PROG = 0
            ans = entry.get()
            break
    return f,ans
def answer_screen(root):
    global CRNT_FRM
    reset(CRNT_FRM)
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="what is the answer?:")
    title.config(font=("Ariel", 18))
    title.grid(row=1, column=0, sticky="NW")
    B = tk.Button(f, text="A", command=lambda :send_ans("A",root))
    B.config(font=("Ariel", 18))
    B.grid(row=2, column=0, sticky="NW")
    B = tk.Button(f, text="B", command=lambda :send_ans("B",root))
    B.config(font=("Ariel", 18))
    B.grid(row=3, column=0, sticky="NW")
    B = tk.Button(f, text="C", command=lambda :send_ans("C",root))
    B.config(font=("Ariel", 18))
    B.grid(row=4, column=0, sticky="NW")
    B = tk.Button(f, text="D", command=lambda :send_ans("D",root))
    B.config(font=("Ariel", 18))
    B.grid(row=5, column=0, sticky="NW")
    CRNT_FRM = f

def between(root,arr):
    global CRNT_FRM
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    print(arr[1])
    if not arr[1] =="0":
        title = tk.Label(f, text="congrats!!!!")
        title.config(font=("Ariel", 18))
        title.grid(row=1, column=0, sticky="NW")
    else:
        title = tk.Label(f, text="fail")
        title.config(font=("Ariel", 18))
        title.grid(row=1, column=0, sticky="NW")
    title = tk.Label(f, text="you gained: " + arr[1])
    title.config(font=("Ariel", 18))
    title.grid(row=2, column=0, sticky="NW")
    title = tk.Label(f, text="total points: " + arr[0])
    title.config(font=("Ariel", 18))
    title.grid(row=3, column=0, sticky="NW")
    title = tk.Label(f, text="your place:" + arr[2])
    title.config(font=("Ariel", 18))
    title.grid(row=4, column=0, sticky="NW")

    CRNT_FRM = f


def client(root):#main loop of the client
   global  CRNT_FRM
   global  SOCK
   global STRT_TIME
   global PROG
   try:
    ip = get_addr(root,0)
    while  ip == "no":
        ip = get_addr(root,0)
    resety(root)
    SOCK = cnct_client(ip,root)
    ans = ""
    wating(root)
    while not ans == "STP":
        ans = all_mesage(SOCK)
        if ans == "STRT":
             STRT_TIME = datetime.datetime.now()
             answer_screen(root)
             point = all_mesage(SOCK).split("_")
             resety(root)
             between(root,point)
    print("congrats u finished game")
    SOCK.close()
    resety(root)
    ending(root,point)
    while True:
        if not PROG == 0:
             break
    if PROG == 1:
         resety(root)
         Kahoot.STAT = 0
         Kahoot.start(root)
    else:
        root.destroy()
   except:
       resety(root)
       error(root)
       while True:
           if not PROG == 0:
               break
       if PROG == 1:
           resety(root)
           Kahoot.STAT = 0
           Kahoot.start(root)
       else:
           root.destroy()

def end():
    global PROG
    PROG = 2

def ending(root,ans):
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="THE END!!!!!!" )
    title.config(font=("Ariel", 18))
    title.grid(row=1, column=0, sticky="NW")
    title = tk.Label(f, text="total points: " + ans[0])
    title.config(font=("Ariel", 18))
    title.grid(row=2, column=0, sticky="NW")
    title = tk.Label(f, text="your place:" + ans[2])
    title.config(font=("Ariel", 18))
    title.grid(row=3, column=0, sticky="NW")
    B = tk.Button(f, text="new game", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=4, column=1, sticky="NW")


    return f

def error(root):
    f = tk.Frame(root)
    f.place(relx=0, rely=0)
    title = tk.Label(f, text="HOST DISCONNECTED :(" )
    title.config(font=("Ariel", 18))
    title.grid(row=1, column=0, sticky="NW")
    B = tk.Button(f, text="new game", command=progress)
    B.config(font=("Ariel", 18))
    B.grid(row=2, column=1, sticky="NW")

    return f


def send_ans(ans,root):
    global SOCK
    global CRNT_FRM
    answer = build_ans(ans)
    SOCK.send(answer.encode())
    CRNT_FRM = wating(root)

def get_addr(root,var):#gets the ip addr based on game pin
    global CRNT_FRM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIP, SPORT))
    if var == 0:
        CRNT_FRM,ans = opening1(root)
    else:
        CRNT_FRM, ans = opening2(root)
    print(ans)
    s.send((build_answer("please")).encode())
    s.send(build_answer(ans).encode())
    addr = all_mesage(s)
    print(addr)
    return addr

def build_ans(ans):
    global STRT_TIME
    start_time = STRT_TIME
    end_time = datetime.datetime.now()
    time_diff = (end_time - start_time)
    execution_time = time_diff.total_seconds() * 1000
    exe = int(execution_time)
    print(exe)
    ans = build_answer(ans + "_" + str(exe))#builds the answer based on protocol len_ans_time
    return ans



def cnct_client(ip,root):#connects client to host based on the ip gotten from server
    global CRNT_FRM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, MPORT))
    CRNT_FRM, name = get_name(root)
    s.send(build_answer(name).encode())  # sends nicname to host
    ans = all_mesage(s)
    while ans == "taken":
        CRNT_FRM, name = get_name2(root)
        s.send(build_answer(name).encode())  # sends nicname to host
        ans = all_mesage(s)

    return s



def all_mesage(sock):#recievs all of the message based on the message length given at the begining of the messsage
    try:
        lent = sock.recv(1).decode()
        if not lent == "":
            while "_" not in lent:
                lent += sock.recv(1).decode()
            lent = int(lent[:-1])#recives the message length
            ans = sock.recv(lent).decode()
            while not len(ans) == lent:
                ans += sock.recv(lent)
            return ans#recieves the message
        else:
            print("host disconnected unexpectedly")
            sock.close()
            client()
    except:
        print("host disconnected unexpectedly")
        sock.close()
        client(root)
def build_answer(ans):#builds apropriate answer according to protocol
    return str(len(ans))+"_"+ans


if __name__ == '__main__':
    try:
        root = set()
        thread = threading.Thread(target=client, args=(root,),daemon=True)  # creates new thread for client
        thread.start()
        root.mainloop()
    except:
        quit()