def med3(a,b,c):
    if a>=b: # 세 정수 중 2개의 수가 같을 수 있는 경우를 고려한 조건문
        if b>=c:
            return b
        elif a<=c:
            return a
        else: 
            return c
    elif a>c:  #b>a의 조건 충족
        return a
    elif b>c: #b>a 와 c>a의 조건 충족
        return c
    else:
        return b
    
print('세 정수의 중앙값을 구하기')
a= int(input('정수 a의 값을 입력하세요.'))
b= int(input('정수 b의 값을 입력하세요.'))
c= int(input('정수 c의 값을 입력하세요.'))

print(f'정수 a,b,c의 중앙값 = {med3(a,b,c,)}')
        
    
