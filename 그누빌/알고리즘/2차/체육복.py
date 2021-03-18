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

    answer1 = [0] * n #체육복을 입을 수 있는 학생 수 기록용
    
    for i in range(n):#0~ n-2까지의 범위 (작은 원소에서 뒤의 원소 비교)
        if i==0: #첫번째 학생의 경우
            if stu[0]>=1:
                answer1[0]=1 #기본값 입력
        if 0<i<n-1: #가운데 원소들인 경우
            if stu[i-1]>1: #앞의 원소에 여유분이 있는 경우
                if stu[i]>1: #현 원소도 여유분이 있는 경우
                    answer1[i]=1
                if stu[i]==0: #현 원소는 여유분 x
                    stu[i-1]-=1 #준 여유분 제외
                    answer1[i]=1 #받은 여유분 추가
                    stu[i]+=1 #받은 여유분 추가
            
            if stu[i-1]==0: #앞 원소에 여유분 x
                if stu[i]>1: #현 원소에 여유분 있는 경우 
                    stu[i]-=1 #준 여유분 제외
                    answer1[i-1]=1 #받은 여유분 추가
                    stu[i-1]+=1 #받은 여유분 추가
            
            if answer1[i]==0 and stu[i+1]>1: #뒤의 원소에 여유분이 있는 경우
                if stu[i]>1: #현 원소에 여유분 있는 경우
                    answer1[i]=1
                if stu[i]==0: #현원소에 여유분 x
                    stu[i+1]-=1 #준여유분 제외
                    answer1[i]=1 #받은 여유분 추가
                    stu[i]+=1
            
            if answer1[i]==0 and stu[i+1]==0:
                if stu[i]>1:
                    stu[i]-=1
                    answer1[i+1]=1 
                    stu[i+1]+=1   
            
        if i==n-1: #마지막 원소인 경우
            if stu[i]>=1:
                answer1[i]=1
    
    result=0 #체육 수업 참여가능한 학생 기록용
    for i in range(n):
        if stu[i] >=1:
            result+=1

    return result      