print('**실습 2C-1 출력')
x = ['John','Goerge','Paul','Ringo']

for i in range(len(x)):
    print(f'x[{i}] = {x[i]}')

print('\n **실습 2C-2 출력')
for i, name in enumerate(x):  # 인자가 반드시 i와 name일 필요는 없다. 다른 문자를 사용해도 무방. 단, 앞의 문자 : 숫자 , 뒤의 문자 : 배열의 원소
    print(f'x[{i}]={name}')

print('\n**실습 2C-3 출력')

for i, name in enumerate(x,1):
    print(f'{i}번째={name}')


print('\n** 실습2C-4 출력')

for i in x:
    print(i)

print('\n** 실험 출력')

for i, n in enumerate(x,1):
    print(f'x[{i}]={n}')

