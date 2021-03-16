
#여벌 옷이 도난 당한 경우의 경우 수도 추가하기(test case7, 10 통과 못한 이유로 추측된다.)

def solution(n, lost, reserve):
    stu = [1] * n #학생 수 만큼 체육복 생성
    lost=list(map(int,lost))
    reserve=list(map(int,reserve))

    for j in range(len(lost)): #0~n까지 : 도난당한 체육복 기록
        if int(lost[j]) >= 1 : #도난당한 학생 번호 파악
            num=int(lost[j])
            stu[num-1]+=-1 #도난당한 번호의 학생 체육복 삭제 (1을 0으로 변경)

    for j in range(len(reserve)):
        if int(reserve[j]) >= 1 :
            num=int(reserve[j])
            stu[num-1]+=1 #여유 분이 있는 학생의 체육복 추가

    answer1 = [0] * n #체육복을 입을 수 있는 학생 수 기록용1
    answer2 = [0] * n #체육복을 입을 수 있는 학생 수 기록용2
    result =0 #최종 수업이 가능한 학생 수 
    
    for i in range(n):#0~ n-2까지의 범위 (작은 원소에서 뒤의 원소 비교)
        if i==0: #첫번째 학생의 경우
            if stu[i]>=1:
                answer1[i]+=1
        else:    
            if stu[i] >=1:
                answer1[i]+=1 
                if stu[i]>1:#stu[i]>1 (여유분이 있는 경우) 
                    if stu[i-1]<1:
                        answer1[i-1]+=1

    #print(answer1)                    
    for i in range(n):#0~ n-2까지의 범위 (작은 원소에서 뒤의 원소 비교) 
        if i!=n-1:
            if stu[i] >=1:
                answer2[i]+=1 
                if stu[i]>1:#stu[i]>1 (여유분이 있는 경우) 
                    if stu[i+1]<1:
                        answer2[i+1]+=1

        else: #마지막번째 학생의 경우
            if stu[i]>=1:
                answer2[i]+=1
    #print(answer2)     

    for i in range(n):
        if answer1[i]>=1 or answer2[i]>=1:
            result+=1
        if (answer1[i]<1 and answer2[i]>=1) or (answer1[i]>1 and answer2[i]<=1) :
            result+=-1
        
    result=int(result)
    return result          


# 2<= n <=30
# 1<=lost <=n (중복x)
# 1<= reserve  <=n(중복x)
# reserve 가 있는 학생만 체육복 대여 가능
# reserve 가 있는 학생도 체육복을 도난당할 수 있다.(단 2개 중 1개만 분실)

if __name__=='__main__':
    n=int(input("학생 수를 입력하시오:"))
    lost=input("도난당한 학생번호를 입력하시오:").split()
    reserve=input("여유 체육복이 있는 학생번호를 입력하시오:").split()
    sol=solution(n,lost,reserve)
    print(f'체육수업을 들을 수 있는 학생의 최대 명 수: {sol}')