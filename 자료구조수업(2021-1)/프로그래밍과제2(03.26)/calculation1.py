class calculator1:
    def __init__(self):
        self.num=0
    def setValue(self,x):
        self.num=x
    def getValue(self):
        return self.num
    def add(self,x):
        self.num+=x
    def sub(self,x):
        self.num-=x
    def mpy(self,x):
        self.num*=x
    def div(self,x):
        self.num//=x
    def mod(self,x):
        self.num%=x
    def clear(self):
        self.num=0
