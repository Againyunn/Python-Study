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


def parenthsesBalance(string):
    s=Stack()
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

                if i==len(string)-1 and s.tt() != []:
                    return fail
    return success

string=input("테스트 할 괄호를 입력하시오 : ")
sol=parenthsesBalance(string)
print(sol)