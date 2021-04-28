yy1, yy2= input().split()
yy1, yy2 = int(yy1), int(yy2)
count=0
for yy in range(yy1, yy2):
    if yy % 400 ==0:
        isLeap = True
    elif yy % 100 ==0:
        isLeap = False
    elif yy % 4 ==0:
        isLeap = True
    else:
        isLeap = False
    
    if isLeap:
        count+=1

print(count)