from heapq import *

f = [int(x) for x in input().split()]
n = len(f)
T = []

for i in range(n):
    heappush(T, (f[i], str(i)))

while len(T) > 1:
    a = heappop(T)
    b = heappop(T)
    heappush(T, (a[0]+b[0], "("+a[1]+" "+b[1]+")"))

s = heappop(T)[1]

#s 를 스택으로 값 연산
depth=[0]*n #깊이

index=0
front=0
back=0
tmp_index=''
for a in range(len(s)-1):
    check1=s[a]
    if check1=='(':
        front=0
        back=0
        for b in range(a+1,len(s)):
            check2=s[b]
            if check2!='(' or check2!=')':
                pass
            if check2=='(':
                front+=1
                pass
            if check2==')':
                back-=1
                pass
    if check1==')': #)일 때 front-=1 해도, (로 시작하면 초기화하여 처음부터 연산
        back+=1

    if check1.isdigit(): #숫자인 경우 비트 수를 depth에 기록
        tmp_index += str(check1)
        if s[a+1].isdigit():
            pass
        else:
            depth[int(tmp_index)]=abs(front+back)
            tmp_index = ''

result=0
for c in range(n):
    result+= depth[c]*f[c]

print(result)






