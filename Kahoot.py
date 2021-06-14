import threading
import tkinter as tk
import Host
import client
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
STAT = 0
PLAYER_NUM = 3
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


def start(root):
    global STAT
    screen(root)
    while True:
        if not STAT == 0:
            break
    resety(root)
    if STAT == 1:
        Host.host(root)
    else:
        client.client(root)







if __name__ == '__main__':
    root = set()
    thread = threading.Thread(target=start, args=(root,),daemon=True)  # creates new thread for client
    thread.start()
    tk.mainloop()