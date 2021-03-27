

class Client(object):
    def __init__(self,name,sock):
        self.name = name
        self.value = 0
        self.added_value = 0
        self.socket = sock

    def Get_name(self):
        return self.name
    def Get_value(self):
        return self.value
    def Get_socket(self):
        return self.socket
    def add_value(self,val):
        self.value += val
    def Set_added_value(self,add):
        self.added_value = add
    def strt_classes(self):
        self.socket.send((str(len("STRT"))+ "_" + "STRT").encode())
    def end_client(self):
        self.socket.send((str(len("STP")) + "_" + "STP").encode())
        self.socket.close()
    def recv_ans(self):
        ans = all_mesage(self.socket)
        ans = ans.split("_")
        return ans[0],ans[1]

    def To_string(self):
        return self.name + ":"+ str(self.value)


def all_mesage(sock):#recievs all of the message based on the message length given at the begining of the messsage
    lent = sock.recv(1).decode()
    while "_" not in lent:
        lent += sock.recv(1).decode()
    print(lent)
    lent = lent[:-1]#recives the message length
    ans = sock.recv(int(lent)).decode()
    print(ans)
    while not len(ans) == int(lent):
        ans += sock.recv(lent)
    return ans#recieves the message