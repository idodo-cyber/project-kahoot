

class Client(object):
    def __init__(self,name,sock):
        self.name = name
        self.value = 0
        self.socket = sock

    def Get_name(self):
        return self.name
    def Get_value(self):
        return self.value


