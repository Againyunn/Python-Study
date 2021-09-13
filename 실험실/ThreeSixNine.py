n = int(input())

for i in range(1, n+1):
    if (i%3 == 0):
        print(0, end=" ")
    elif (i%10) != 0 and ((i%10)%3 == 0):
        print(0, end=" ")
    elif i>10 and (i-(i%10))%3 == 0:
        print(0, end=" ")
    else:
        print(i, end=" ")