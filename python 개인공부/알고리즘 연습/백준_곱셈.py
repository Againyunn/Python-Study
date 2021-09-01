first = list(input())
second = list(input())

fisrt=list(map(int, first))
second=list(map(int, second))

num=max(len(first),len(second))
list_answer=[]

for u in range(num):
    list_answer.append(0)

for i in range(len(second)-1,-1,-1):
    temp=0
    c1=0
    for j in range(len(first)-1,-1,-1):
        temp= second[i] * fisrt[j]
        list_answer[i]+=temp*(10**(c1))
        c1+=1
        temp=0

Sum=0
c2=0
for k in range(len(list_answer)-1,-1,-1):
    print(list_answer[k])
    Sum+=(list_answer[k]*(10**c2))
    c2+=1
print(Sum)

