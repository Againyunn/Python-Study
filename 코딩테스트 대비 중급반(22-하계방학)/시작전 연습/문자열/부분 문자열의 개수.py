str_a = input()
str_b = input()

len_str_a = len(str_a)
len_str_b = len(str_b)

tmp =str_a[0]
result = 0
for i in range(1, len_str_a):
    tmp += str_a[i]

    #b문자열보다 문자 수가 적은 경우
    if len(tmp) < len_str_b: 
        continue
    
    #b문자열과 문자 수가 같은 경우
    elif len(tmp) == len_str_b:
        #b문자열과 tmp가 같은 경우
        if tmp == str_b:
            result += 1
            
        #초기화
        tmp = str_a[i]
        count = 0

print(result)