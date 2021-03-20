import socket
import random
import threading
IP = "0.0.0.0"
PORT = 55368
ACTIVEREQ={}
lock = threading.Lock()

def findkey(val):
    key_list = list(ACTIVEREQ.keys())
    print(key_list)
    val_list = list(ACTIVEREQ.values())
    print(val_list)
    return key_list[val_list.index(int(val))]

def handleactive(c,addr):#assigns an active client a personalized id,and closes connection when finished
    num = random.randint(100000,999999)
    while num in ACTIVEREQ.values():
        num = random.randint(100000, 999999)
    lock.acquire()
    ACTIVEREQ[addr[0]] = num #assigns the client a personalized number code and lists him as an active client
    lock.release()
    c.send(str((ACTIVEREQ[addr[0]])).encode())#sends the active client his personalized password
    print(ACTIVEREQ)
    txt = c.recv(1024).decode()#waits until the active client responds(will delete the client from actives even when there is an unexpected disconnection
    if txt == "bye":
        lock.acquire()
        del ACTIVEREQ[addr[0]]  # assigns the client a personalized number code and lists him as an active client
        lock.release()
        print("disconnected client")
    elif txt == "":
        lock.acquire()
        del ACTIVEREQ[addr[0]]  # assigns the client a personalized number code and lists him as an active client
        lock.release()
        print("client disconnected")
    c.close()



def handlepasive(c):#sends to the passive client the ip address of the active client with the desired number
    param = c.recv(1024).decode()
    try:
        lock.acquire()
        saddr = findkey(param)#finds the corresponding ip for the num
        lock.release()
    except:
        saddr = "no"
    c.send(saddr.encode())
    c.close()

def handle(c,addr):#understands what client and assigns command accordingly
    txt = (c.recv(1024)).decode()
    if txt == "hello":
        handleactive(c,addr)
    elif txt == "please":
        handlepasive(c)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP,PORT))
    while True:
        s.listen()
        c, addr = s.accept()
        print("here")
        thread = threading.Thread(target = handle,args = (c,addr))
        thread.start()

if __name__ == '__main__':
    main()

