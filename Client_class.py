class Client(object):
    def __init__(self, name, sock):
        self.name = name
        self.value = 0
        self.added_value = 0
        self.socket = sock

    def add_value(self, val):
        self.value += val

    def set_added_value(self, add):
        self.added_value = add

    def strt_classes(self):
        self.socket.send((str(len("STRT")) + "_" + "STRT").encode())

    def end_client(self):
        self.socket.send((str(len("STP")) + "_" + "STP").encode())
        self.socket.close()

    def recv_ans(self):
        ans = all_message(self.socket)
        ans = ans.split("_")
        return ans[0], ans[1]

    def __str__(self):
        return self.name + ":" + str(self.value)


def all_message(sock):  # receives all of the message based on the message length given at the begining of the messsage
    lent = sock.recv(1).decode()
    while "_" not in lent:
        lent += sock.recv(1).decode()
    print(lent)
    lent = lent[:-1]  # receives the message length
    ans = sock.recv(int(lent)).decode()
    print(ans)
    while len(ans) != int(lent):
        ans += sock.recv(lent)
    return ans  # receives the message
