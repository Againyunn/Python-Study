class Stack:
    def __init__(self):
        self.items = []
        
    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, e):
        self.items.append(e)
#        print("test", (sys.getsizeof(self.items)))

    def pop(self):
        try:       
            return self.items.pop()
        except IndexError:
            print('Stack is empty')


def precedence(op):
    if op=='(' or op==')':
        return 0
    if op=='+' or op=='-' : 
        return 1
    if op=='+' or op=='/' :
        return -1
    
def Infix2Postfix(expr):
    s = Stack()
    output=[]
    for term in expr:
        if term in '(':
            s.push('(')
            
        elif term in ')':
            while not s.isEmpty():
                op=s.pop()
                if op =='(':
                    break
                else:
                    output.append(op)
        
        elif term in "+-*/":
            while not s.isEmpty():
                op= s.peek()
                if(precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else:
                    output.append(term)
        
        while not s.isEmpty():
            output.append(s.pop())

        return output
                
sik="((2+3)/5)"
sol=Infix2Postfix(sik)
print(sol)
