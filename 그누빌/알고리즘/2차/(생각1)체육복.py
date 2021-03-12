# 2<= n <=30
# 1<=lost <=n (중복x)
# 1<= reserve  <=n(중복x)
# reserve 가 있는 학생만 체육복 대여 가능
# reserve 가 있는 학생도 체육복을 도난당할 수 있다.(단 2개 중 1개만 분실)

def solution(n, lost, reserve):
    stu = [1] * n #학생 수 만큼 체육복 생성

    for j in range(len(lost)): #0~n까지 : 도난당한 체육복 기록
        if int(lost[j]) >= 1 : #도난당한 학생 번호 파악
            num=int(lost[j])
            stu[num-1] = 0 #도난당한 번호의 학생 체육복 삭제 (1을 0으로 변경)
    print(stu) #테스트 용

    for j in range(len(reserve)):
        if int(reserve[j]) >= 1 :
            num=int(reserve[j])
            stu[num-1]+=1 #여유 분이 있는 학생의 체육복 추가
    
    print(stu) #테스트 용
    answer = 0 #체육복을 입을 수 있는 학생 수 기록용
    
    for i in range(n):#0~ n-2까지의 범위
        if i==0: #첫번째 학생의 경우
            if stu[i]==1:
                answer+=1
                print(answer) #테스트 용
        elif stu[i] >=1:
            answer+=1 
            print(answer) # 테스트 용
            if stu[i]>1:#stu[i]>1 (여유분이 있는 경우) 
                if stu[i-1]==0:
                    answer+=1
                    print(answer) # 테스트 용
    return answer            


if __name__=='__main__':
    n=int(input("학생 수를 입력하시오:"))
    lost=list(input("도난당한 학생번호를 입력하시오:"))
    reserve=list(input("여유 체육복이 있는 학생번호를 입력하시오:"))
    sol=solution(n,lost,reserve)
    print(sol)