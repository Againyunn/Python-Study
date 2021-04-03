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
    ###테스트 목적 : 리스트 출력
    #def tt(self): 
    #    return self.items


def parenthsesBalance(string):
    s=Stack()
    openParenthesis = '({['
    closeParenthesis = ']})'
    success=1
    fail=0
    error=['error1','error2','error3','error4','error5','error6']

    for i in range(len(string)): 
        ch=string[i]
        #print(f'순서: {i} ,ch : {ch}')
        if ch in openParenthesis: #ch가 여는 괄호 중 하나인 경우
            s.push(ch)
        elif ch in closeParenthesis: #ch가 '공백'이거나 '닫는 괄호 중 하나'인 경우
            if s.isEmpty()==True: #스택이 비어있는 경우
                if ch =='(':
                    return i ,error[3]
                elif ch =='{':
                    return i ,error[4]
                elif ch =='[':
                    return i ,error[5]
                elif ch ==')':
                    return i, error[0]
                elif ch =='}':
                    return i, error[1]
                elif ch ==']':
                    return i, error[2]

            else: #스택이 비어있지 않은 경우
                openCh=s.pop() 
                #print(f'openCh : {openCh}')
                if (ch==')' and openCh !='(') :
                    return i ,error[0]
                elif ch=='}' and openCh !='{':
                    return i ,error[1]
                elif ch ==']' and openCh !='[' :
                    return i ,error[2]
                elif ch =='' and i==len(string)-1:
                    if openCh =='(':
                        return i ,error[3]
                    elif openCh =='{':
                        return i ,error[4]
                    elif openCh =='[':
                        return i ,error[5]
    #print(s.tt())
    return success

string=input("테스트 할 괄호를 입력하시오 : ")
sol=parenthsesBalance(string)
print(sol)

                    #if s.tt() != []: