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
        #return self.items.pop() 
        if self.isEmpty():
            return 0 #비었다고 표시 error 처리를 위해 0으로 반환하도록 설정
        else:
            try:
                return self.items.pop() #items에서 삭제 후 반환
            except IndexError:
                return 0 #비었다고 표시 error 처리를 위해 0으로 반환하도록 설정
    def size(self):
        return len(self.items)
        ###테스트 목적 : 리스트 출력
    def tt(self): 
        return self.items

def evalPostfix(expr):
    print(expr)
    s = Stack()
    parenthesis = ['+','-','*','//']  
    for token in expr:
        print(s.tt())
        if token in parenthesis:
            print(token)
            val2 = s.pop()
            val1 = s.pop()
            val2=float(val2)
            val1=float(val1)
            print(f'val1 : {val1} , val2 : {val2}')
            if (token =='+'): 
                if val1==0:
                    answer='error'
                    return answer
                i = val1+val2
                s.push(i)
            elif (token =='-'):
                if val1==0:
                    answer='error'
                    return answer
                i = val1-val2
                s.push(i)
            elif (token =='*'):
                if val1==0:
                    answer='error'
                    return answer
                i = val1 * val2
                s.push(i)
            elif (token =='//'):
                if val1==0:
                    answer='error'
                    return answer
                i = val1 // val2
                s.push(i)
        else: # ; 을 입력받은 경우
            if token==';':
                t=s.pop()
                if t%t==0:
                    answer=int(t)
                else:
                    answer=float(t)
                return answer
            s.push(float(token))
            

    

expr=input("테스트 할 괄호를 입력하시오 : ").split()
sol=evalPostfix(expr)
print(sol)