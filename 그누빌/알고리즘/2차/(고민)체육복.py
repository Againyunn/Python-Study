
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
    asr1=0
    
    for i in range(1,n+1):
        if i==1: #첫번째 학생의 경우
            if stu[i]==1: #첫번째 학생의 체육복 1개 
                answer1[i]+=1
            if stu[i]>1: #첫번째 학생이 체육복 2개
                if answer1[i]!=2:#i번째 학생이 타 학생에게 체육복을 받지 않은 경우
                    if stu[i+1]==0:#두번째 학생이 체육복 없을 때
                        answer1[i+1]+=1
    
        if i==2 or i==n-1: #두번째 학생과 뒤에서 두번째 학생의 경우
            if stu[i]==1:
                answer1[i]+=1
            if stu[i]>1:
                answer1[i]+=1
                if answer1[i]!=2:#i번째 학생이 타 학생에게 체육복을 받지 않은 경우
                    if stu[i-1]==0 and stu[i+1]>0: #이전 학생의 체육복이 없고, 다음 학생의 체육복이 있는 경우
                        answer1[i-1]+=1
                    if stu[i-1]>0 and stu[i+1]==0: #이전 학생의 체육복이 있고, 다음 학생의 체육복이 없는 경우
                        answer1[i+1]+=1
        if i>2 or i<n-1:    #3번째~뒤에서 3번째까지의 모든 학생
            if stu[i]==1:
                answer1[i]+=1
            if stu[i]>1:
                answer1[i]+=1
                if answer1[i]!=2:#i번째 학생이 타 학생에게 체육복을 받지 않은 경우
                    if stu[i-1]==0 and stu[i+1]>0: #이전 학생의 체육복이 없고, 다음 학생의 체육복이 있는 경우
                        answer1[i-1]+=1
                    if stu[i-1]>0 and stu[i+1]==0: #이전 학생의 체육복이 있고, 다음 학생의 체육복이 없는 경우
                        answer1[i+1]+=1
                    if stu[i-1]==0 and stu[i+1]==0: #양쪽 다 체육복이 없는 경우
                        if stu[i-2]>0: # 이전 학생은 체육복을 받을 수 있는 경우
                            answer1[i+1]+=1 #다음 학생에게 체육복 주기
                        if stu[i+2]>0: # 다음 학생은 체육복을 받을 수 있는 경우
                            answer1[i-1]+=1 #이전 학생에게 체육복 주기
        if i==n: #마지막 번째 학생
            if stu[i]==1: #마지막번째 학생의 체육복 1개 
                answer1[i]+=1
            if stu[i]>1: #마지막번째 학생이 체육복 2개
                if answer1[i]!=2:#i번째 학생이 타 학생에게 체육복을 받지 않은 경우
                    if stu[i-1]==0: #뒤에서 두번째 학생이 체육복 없을 경우
                        answer1[i-1]+=1
                
    for i in answer1:
        if i >=1:
            asr1+=1
    
    return asr1       


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