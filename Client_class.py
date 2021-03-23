

class Client(object):
    def __init__(self,name,sock):
        self.name = name
        self.value = 0
        self.socket = sock

    def Get_name(self):
        return self.name
    def Get_value(self):
        return self.value

    def To_string(self):
        return self.name + ":"+ str(self.value)


def all_mesage(sock):#recievs all of the message based on the message length given at the begining of the messsage
    lent = sock.recv(1)
    while "_" not in lent:
        lent += sock.recv(1)
    lent = lent[:-2]#recives the message length
    ans = sock.recv(lent)
    while not len(ans) == int(lent):
        ans += sock.recv(lent)
    return ans#recieves the message