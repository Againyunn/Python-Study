import numpy

def Diagram(B,A, num):
    A.sort() #오름차순 정렬
    tmp=[0 for x in range(B)] #각 블록 리스트 DP저장용
    interval=[] # 각 원소 간의 간격(차이) 기록용
    max_interval=0 # 최대 간격(차이)
    max_index=0 # 최대 간격일 때의 원소 인덱스
    for i in range(1,num): #최대 간격 찾기
        tmp = 0
        this_interval =abs(A[i-1] - A[i])
        interval.append(this_interval)
        tmp+=1
        if this_interval>max_interval:
            max_interval=this_interval
            max_index = (num-tmp-1)

    first=[] #첫번째 블록
    second=[] #두번째 블록
    for j in range(num): #각 블록별 list 나누어 담기
        if j < max_index:
            first.append(A[j])
        else:
            second.append(A[j])

    #각 블록별 평균기록
    first_avr=numpy.mean(first)
    second_avr=numpy.mean(second)

    result=0
    for k in range(num): #오차의 합
        if k <max_index:
            result+=(A[k]-first_avr)**2
        else:
            result+=(A[k]-second_avr)**2


    return round(result,3)

check = list(map(int,input().split()))
B = check[0] #나누는 블럭 수
num = check[1] #원소 수
A=[] #리스트
for i in range(num):
    A.append(int(input()))
print(Diagram(B,A, num))

#####
# B-1회 반복 & [n-(B-1) : 0] n-B+1부터 0번째 인덱스까지 입력받은 리스트(A)의 원소들을 B개의 블록으로 각각 나눈다는 규칙은 발견했습니다.
# ex)
# 입력값: B = 2, n = 8 인경우
# 2 / 3 4 5 6 6 12 16
# 2 3 / 4 5 6 6 12 16
# 2 3 4 / 5 6 6 12 16
# 2 3 4 5 / 6 6 12 16
# 2 3 4 5 6 / 6 12 16
# 2 3 4 5 6 6 / 12 16
# 2 3 4 5 6 6 12 / 16

# 입력값: B =3, n = 8 인경우
# 1 / 2 / 3 4 5 6 7 8
# 1 / 2 3 / 4 5 6 7 8
# 1 / 2 3 4 / 5 6 7 8
# 1 / 2 3 4 5 / 6 7 8
# 1 / 2 3 4 5 6 / 7 8
# 1 / 2 3 4 5 6 7 / 8
# 1 2 / 3 / 4 5 6 7 8
# 1 2 / 3 4 / 5 6 7 8
# 1 2 / 3 4 5 / 6 7 8
# 1 2 / 3 4 5 6 / 7 8
# 1 2 / 3 4 5 6 7 / 8
# 1 2 3 / 4 / 5 6 7 8
# 1 2 3 / 4 5 / 6 7 8
# 1 2 3 / 4 5 6 / 7 8
# 1 2 3 / 4 5 6 7 / 8
# 1 2 3 4 / 5 / 6 7 8
# 1 2 3 4 / 5 6 / 7 8
# 1 2 3 4 / 5 6 7 / 8
# 1 2 3 4 5 / 6 / 7 8
# 1 2 3 4 5 / 6 7 / 8
# 1 2 3 4 5 6 / 7 / 8
#
# 등의 방식으로 비교가 이루어진다는 것을 확인했지만, 변화하는 값에 대한 알맞은 DP 테이블 구축 방법을 찾지 못하여 문제를 완전히 풀지 못했습니다.
# 작성된 코드 수행시간 : O(n^2)
# 완전한 DP테이블을 구축할 때의 실제 코드 예상 수행 시간 O(n^2 * logn)

