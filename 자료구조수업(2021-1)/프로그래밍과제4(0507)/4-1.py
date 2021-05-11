class Node:
    def __init__(self,e):
        self.data=e
        self.link = None

class LinkedStack:
    def __init__ (self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self, e):
        newNode = Node(e)
        newNode.link= self.top
        self.top = newNode
    
    def pop(self):
        if(self.isEmpty()):
            print("Stack is empty")
            return
            
        e = self.top.data
        self.top=self.top.link
        return e

def solution(string):
    s=LinkedStack()
    openParenthesis = '({['
    closeParenthesis = ']})'
    success=1
    fail=0

    for i in range(len(string)): 
        ch=string[i]
        
        if ch in openParenthesis: #ch가 여는 괄호 중 하나인 경우
            s.push(ch)
        elif ch in closeParenthesis: #ch가 '공백'이거나 '닫는 괄호 중 하나'인 경우
            if s.isEmpty()==True: #스택이 비어있는 경우
                return fail
            else: #스택이 비어있지 않은 경우
                openCh=s.pop() 
                if (ch==')' and openCh !='(' or ch=='}' and openCh !='{' or ch ==']' and openCh !='[' or openCh=="True"):
                    return fail
    return int(s.isEmpty())

string=input()
sol=solution(string)
print(sol)