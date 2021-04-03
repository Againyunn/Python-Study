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
            return True #비었다고 표시
        else:
            try:
                return self.items.pop() #items에서 삭제 후 반환
            except IndexError:
                return True #비었다고 표시
    def size(self):
        return len(self.items)

def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in "+-*/":
            val2 = s.pop()
            val1 = s.pop()
            if (token =='+'): 
                s.push(val1 + val2)
            elif (token =='-'):
                s.push(val1 - val2)
            elif (token =='+'):
                s.push(val1 * val2)
            elif (token =='/'):
                s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()

