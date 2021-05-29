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
    c.send(build_ans(str((ACTIVEREQ[addr[0]]))).encode())#sends the active client his personalized password
    print(ACTIVEREQ)
    txt = all_mesage(c)#waits until the active client responds(will delete the client from actives even when there is an unexpected disconnection
    if txt == "bye":
        lock.acquire()
        del ACTIVEREQ[addr[0]]  # deletes the host from dictionary thus allowing for the pin to be used
        lock.release()
        print("disconnected client")
    elif txt == "":
        lock.acquire()
        del ACTIVEREQ[addr[0]]  # deletes the host from dictionary thus allowing for the pin to be used
        lock.release()
        print("client disconnected")
    c.close()



def handlepasive(c):#sends to the passive client the ip address of the active client with the desired number
    param = all_mesage(c)
    print(param)
    lock.acquire()
    try:

        saddr = findkey(param)#finds the corresponding ip for the num

    except:
        saddr = "no"
    lock.release()
    c.send(build_ans(saddr).encode())
    c.close()

def handle(c,addr):#understands what client and assigns command accordingly
    txt = all_mesage(c)
    if txt == "hello":
        handleactive(c,addr)
    elif txt == "please":
        handlepasive(c)
def build_ans(ans):
    return str(len(ans))+"_"+ans

def all_mesage(sock):#recievs all of the message based on the message length given at the begining of the messsage
    lent = sock.recv(1).decode()
    while "_" not in lent:
        lent += sock.recv(1).decode()
    lent = int(lent[:-1])#recives the message length
    ans = sock.recv(lent).decode()
    while not len(ans) == lent:
        ans += sock.recv(lent)
    return ans#recieves the message


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((IP,PORT))
    print("server is up and runing")
    while True:
        s.listen()
        c, addr = s.accept()
        thread = threading.Thread(target = handle,args = (c,addr))
        thread.start()


if __name__ == '__main__':
    main()