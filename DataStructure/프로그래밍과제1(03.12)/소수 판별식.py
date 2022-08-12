def solution(n):
    num=[]#값의 집합
    for i in range(n//2,n+1): #1~n까지의 수들로 원소 형성(0은 연산해도 소수가 아니기때문)
        for j in range(1,n//2+1):
            if i>=j: #두 수가 중복되지 않도록 크기를 지정
                if n==i+j:
                    num.append([i,j]) # 합이 n이 되는 두 수를 저장

    number=[] #중복을 제거(합이 n이 되는 두 수를 저장)
    for i in range(len(num)):
        for j in range(len(num)):
            if [num[i][0],num[i][1]]!=number:
                number.append([num[i][0],num[i][1]])

    #n까지의 소수 판별
    pri=[]
    for A in range(2, n+1): #2부터 1000까지 범위의 수
        for i in range(2, n+1): #n까지의 수 중 i로 지정된 숫자마다의 값을 대입
            if A % i ==0: #만약 A / i 했을 때 0의 값이 나온다면 소수임이 맞으므로 if의 순환을 멈춘다.
                pri.append(i)
                break
    
    pri = list(set(pri))
    result =[]#결과 값을 담을 list

    for i in range(len(num)): #합이 n이 되는 두 수 list
        for j in range(len(pri)): #n까지의 소수 list
            for k in range(len(pri)):
                if num[i][0]==pri[j] and num[i][1]==pri[k]:
                    #if num[i][0]<=num[i][1]: #중복 값을 제거하고 오름차순으로 두 수를 정렬
                    print(num[i][0] , num[i][1])
                    result.append(num[i])

    answer=[] #최종답
    for i in range(len(result)):
        for j in range(len(result)):
            while result[i][1]-result[i][0] >= result[j][1]-result[j][0]:
                break 
        break
    answer.append(result[i])
    
    answer1=answer[0][0]
    answer2=answer[0][1]

    return answer1 , answer2

if __name__=='__main__':
    n=int(input('정수를 입력하시오: '))
    sol=solution(n)
    print(sol)
    

                


                


