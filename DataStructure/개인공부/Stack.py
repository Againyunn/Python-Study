class Stack:
    def __init__ (self):
        self.items=[]
    def isEmpty(self):
        return len(self.items) == 0
    def clear(self):
        self.items=[]
    def push(self,e):
        self.items.append(e)
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            try:
                return self.items.pop()
            except IndexError:
                print("Stack is empty")
    def size(self):
        return len(self.items)