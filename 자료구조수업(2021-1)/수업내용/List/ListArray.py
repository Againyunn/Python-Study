#주의: 파이썬 기본 함수 list와는 다른 list 형태
class ArrayList:
    def __init__(self):
        self.items=[]
    def insert(self, pos, element):
        self.items.insert(pos,element)
    def delete(self, pos):
        return self.items.pop(pos)
    def isEmpty(self):
        return self.size()==0
    def getEntry(self, pos):
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]
    def find(self, item):
        return self.items.index(item)
    def replace(self, pos, element):
        self.items[pos]=element
    def sort(self):
        self.items.sort()
    def merge(self, lst):
        self.items.extend(lst)
    def display(self, msg='ArrayList'): #입력 받을 message를 사용자로부터 입력받을 수 있는 기능
        print(msg, '항목수=', self.size(), self.items)

s=ArrayList()
s.insert(0,1)
s.insert(1,2)
s.insert(2,3)
s.display("파이썬 리스트로 구현한 리스트")