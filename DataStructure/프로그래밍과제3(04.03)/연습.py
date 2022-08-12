num=[1,2,3,4,5,6]
sum1=0
check=0
for i in num:
    for j in num:
        for k in num:
            sum1+=i*100 + j *10 +k
            check+=1
print(sum1)
print(check)
avr=sum1/check
print(avr)
print("*****")

num1=[1,2,3,4,5,6,7,8,9]
sum2=0
check1=0
for i in num1:
    for j in num1:
        for k in num1:
            sum2+=i*100 + j *10 +k
            check1+=1
avr1=sum2/check1
print(sum2)
print(check1)
print(avr1)