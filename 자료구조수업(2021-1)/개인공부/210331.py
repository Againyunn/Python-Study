from Stack import Stack

def parenthsesBalance(string):
    s=Stack()
    openParenthesis = '({['
    closeParenthesis = ']})'
    for ch in string: 
        if ch in openParenthesis:
            s.push(ch)
        elif ch in closeParenthesis:
            if s.isEmpty():
                return False
            else:
                openCh=s.pop()
                if(ch==')' and openCh !='(' or ch=='{' and openCh !='}' or ch =='[' and openCh !=']'):
                    return False
    return s.isEmpty()


string=input("테스트 할 괄호를 입력하시오 : ")
sol=parenthsesBalance(string)
print(sol)