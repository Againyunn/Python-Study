class Stack:
    def __init__(self):
        self.items = []
    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return self.__len__() == 0


def get_token_list(expr):
    res = []
    temp = ''
    
    for i in expr:
        if i in ['+','-','*','/','^','(',')'] :
            if temp != '' :
                res.append(float(temp))
                temp = ''
            res.append(i)
        elif (i == '.') or (i.isdigit()) :
            temp += i
        else :
            continue

    if temp != '' :
        res.append(float(temp))
    
    return res


def infix_to_postfix(token_list):
    opstack = Stack() #연산자 저장 스택
    outstack = []     #결과값 저장 스택
    
    # 연산자의 우선순위 설정
    prec = {}
    prec['('] = 0
    prec['+'] = 1
    prec['-'] = 1
    prec['*'] = 2
    prec['/'] = 2
    prec['^'] = 3

    for token in token_list:
        if token == '(': # ( 스택에 넣기)
            opstack.push(token)
        elif token == ')': #( 까지 pop한걸 outstack에 넣기 
            while (not opstack.isEmpty()) and opstack.top() != '(':
                outstack.append(opstack.pop())
            opstack.pop()
        elif token in ['+','-','*','/','^'] :
            while (not opstack.isEmpty()) and prec[token] <= prec[opstack.top()]:
                outstack.append(opstack.pop())
            opstack.push(token)        
        else:  # operand일 때
            outstack.append(token)

    while (not opstack.isEmpty()):
        outstack.append(opstack.pop())

    return outstack

def compute_postfix(token_list):

    #nStack = 숫자스택
    nStack = Stack()

    for token in token_list:


        if token in ['+','-','*','/','^']: #연산자일 경우 계산
            a = float(nStack.pop())
            b = float(nStack.pop())
            
            if token == '+' :
                nStack.push(b+a)
            if token == '-' :
                nStack.push(b-a)
            if token == '*' :
                nStack.push(b*a)
            if token == '/' :
                nStack.push(b/a)
            if token == '^' :
                nStack.push(b**a)

        else : #숫자일 경우
            nStack.push(token)



    res = nStack.pop()
    
    if not nStack.isEmpty() :
        print("Wrong!")
    
    return res

   
# 아래 세 줄은 수정하지 말 것!
expr = input()
value = compute_postfix(infix_to_postfix(get_token_list(expr)))
print(value)