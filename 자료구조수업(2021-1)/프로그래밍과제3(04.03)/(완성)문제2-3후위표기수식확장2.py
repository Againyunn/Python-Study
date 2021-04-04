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
            answer='fail'
            return answer #비었다고 표시 error 처리를 위해 0으로 반환하도록 설정
        else:
            try:
                return self.items.pop() #items에서 삭제 후 반환
            except IndexError:
                answer='fail'
                return answer #비었다고 표시 error 처리를 위해 0으로 반환하도록 설정
    def size(self):
        return len(self.items)
        ###테스트 목적 : 리스트 출력
    #def tt(self): 
    #    return self.items

def evalPostfix(expr):
    #print(expr)
    s = Stack()
    parenthesis = ['+','-','*','//']  
    for i in range(len(expr)):
        token=expr[i]
        #print(s.tt())

        #set 명령어
        if expr[0]=='set': #expr의 index0은 스택에 저장x  
            #token = 연산자
            if token in parenthesis:
                #print(token)
                val2 = s.pop()
                val1 = s.pop()
                val2=float(val2)
                try:
                    val1=float(val1)
                except ValueError:
                    val1=0
                #print(f'val1 : {val1} , val2 : {val2}')
                if (token =='+'): 
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1+val2
                    s.push(i)
                elif (token =='-'):
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1-val2
                    s.push(i)
                elif (token =='*'):
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1 * val2
                    s.push(i)
                elif (token =='//'):
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1 // val2
                    s.push(i)

            #token = ;
            elif token==';':
                t1=s.pop()#연산자로 계산된 마지막 피연산자 값 pop
                t2=s.pop()
                if t2=='fail': #연산의 결과 값을 앞서 입력받은 알파벳(문자)var에 참조(dictionary 이용)
                    varBox={}
                    if t1%t1==0:
                        varBox[var]=int(t1) #입력된 문자가 해당 참조 값을 참고
                    elif t1%t1!=0:
                        varBox[var]=float(t1)
                elif t2!='fail': #연산을 모두 했음에도 불구하고 피연산자가 스택에 남은 경우
                    answer='error2'
                    return answer

            #token = 문자
            elif str(token).isalpha():
                var=str(token) #문자를 var로 저장(스택에 push x)
            
            #token = 숫자
            else:
                s.push(float(token))
    #eval 경우
        if expr[0]=='eval': #expr의 index0은 스택에 저장x         
            #token = 연산자
            if token in parenthesis:
                #print(token)
                val2 = s.pop()
                val1 = s.pop()
                val2=float(val2)
                try:
                    val1=float(val1)
                except ValueError:
                    val1=0
                #print(f'val1 : {val1} , val2 : {val2}')
                if (token =='+'): 
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1+val2
                    s.push(i)
                elif (token =='-'):
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1-val2
                    s.push(i)
                elif (token =='*'):
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1 * val2
                    s.push(i)
                elif (token =='//'):
                    if val1==0:
                        answer='error1'
                        return answer
                    i = val1 // val2
                    s.push(i)

            #token = ;
            elif token==';':
                t1=s.pop()#연산자로 계산된 마지막 피연산자 값 pop
                t2=s.pop()
                if t2=='fail': #연산의 결과 값을 앞서 입력받은 알파벳(문자)var에 참조(dictionary 이용)
                    varBox={}
                    if t1%t1==0:
                        answer=int(t1) #입력된 문자가 해당 참조 값을 참고
                    elif t1%t1!=0:
                        answer=float(t1)
                elif t2!='fail': #연산을 모두 했음에도 불구하고 피연산자가 스택에 남은 경우
                    answer='error2'
                return answer

            #token = 문자
            elif str(token).isalpha():
                var=str(token) #문자를 var로 저장(스택에 push x)
            
            #token = 숫자
            else:
                s.push(float(token))
    #quit 경우
        if expr[0]=='quit': #expr의 index0은 스택에 저장x 
            break #for문 탈출 후 함수 종료



expr=input("테스트 할 값을 입력하시오 : ").split()
sol=evalPostfix(expr)
print(sol)