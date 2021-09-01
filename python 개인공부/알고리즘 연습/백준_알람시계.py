num = list(input().split())
num_list = list(map(int,num))

if num_list[1]-45<0:
    temp1=num_list[1]
    num_list[1]=(temp1-45)+60
    num_list[0]-=1
else:
    num_list[1]-=45
    
if num_list[0]<0:
    temp2=num_list[0]
    num_list[0]=temp2+24


print(f'{num_list[0]} {num_list[1]}')