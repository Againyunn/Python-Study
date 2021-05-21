def solution(prices):
    stack=[]
    answer = prices
    check=0
    stack.append(prices[0])
    
    for i in range(1, len(prices)):
        check+=1
        stack.append(prices[i])
        print(f'정상 : check :{check},  원소 : {prices[i]}')
        if prices[i-1]> prices[i]:
            t1=stack.pop()
            answer[prices.index(t1)] = len(stack) - check
            check=0
            print(f'하락 : check : {check},  원소 : {t1} ')
    
    print(stack)
    num=len(stack)
    for j in range(num):
        t2=stack.pop()
        answer[prices.index(t2)] = len(stack)-1
        print(f'체크 : 원소 : {t2}')
    
    return answer

i=input().split()
sol=solution(i)
print(i)