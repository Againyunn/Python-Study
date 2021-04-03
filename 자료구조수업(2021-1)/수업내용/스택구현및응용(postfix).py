# import sys
'''
expr1 =""

for x in expr:
    if x in '+-*/;':
        expr1 = expr1 + ' ' + x + ' '
    else:
        expr1 = expr1 + x
'''




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
            
#postfix evaluation

def evaluation(expr):
    s = Stack()    
    op = '+-*/' #op = ('+','-','*','/') 
    for item in expr:
        if item in op:
            right_opr = s.pop()
            left_opr = s.pop()  # operand: 피연산자, operator: 연산자
            if item == '+':
                s.push(left_opr+right_opr)
            elif item == '-':
                s.push(left_opr-right_opr)
            elif item == '*':
                s.push(left_opr*right_opr)                
        elif item == ';':
            break
        else:
#        item = int(item)
            s.push(int(item))
    return s.pop()

# 입력 수식의 피연산자 연산자 사이에 공백이 있음: 20 30 - 15 * ;
# 수식의 마지막은 ;으로 끝남 '20 30 - 15 * ;'

expr = input().split() # expr: ['20','30','-','15','*',';']
result = evaluation(expr)
print(result)
    
       
            
'''
s = Stack()

n = int(input())

while n!= 0 :
    s.push(n%2)
    n //= 2


while not s.isEmpty():
    digit = s.pop()
    print(digit, end = '')

'''

