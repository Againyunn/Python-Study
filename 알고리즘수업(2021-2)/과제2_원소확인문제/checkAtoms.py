'''첫번째 #은 주석, 두번째 #은 각 구문/반복문 별 시간복잡도입니다.'''

def two_sum(X,Y,t):
    # 각 리스트별 원소 수(A -> X, B -> Y) #+2
    len_x=len(X)-1
    len_y=len(Y)-1

    # 2진 탐색을 위한 시작/끝 인덱스 설정_X리스트 #+2
    start_x=0
    end_x=len_x

    # 2진 탐색을 위한 시작/끝 인덱스 설정_Y리스트 #+2
    start_y=0
    end_y=len_y

    # 함수 결과 반환용 변수 : X(임의 원소)+Y(임의 원소) = t 를 만족하기 전까지 default값 #+1
    answer=False

    '''기본 원리: (while 문 이하) 
       X와Y의 인덱스 중위값을 항상 pivot으로 설정하여 X[pivot]+Y[pivot]의 값이 t와 같은 지 확인
       경우0:
       X[pivot]+Y[pivot]=t으로 조건 만족 상태
       경우1: 
       X[pivot]+Y[pivot]<t이면 X와 Y의 값을 기존 pivot보다 앞의 인덱스들 중 중간 값을 새로운 pivot으로 지정하여 반복 연산
       경우2:
       X[pivot]+Y[pivot]>t이면 X와 Y의 값을 기존 pivot보다 뒤의 인덱스들 중 중간 값을 새로운 pivot으로 지정하여 반복 연산
       * 각 경우1, 경우2 모두 X의 원소값을 먼저 탐색한 뒤 만족되지 않으면 Y원소 탐색
       경우3:
       X[모든 원소들 확인]+Y[모든 원소들 확인] != t 조건 불만족인 상태"'''
    while True: #*nlogn
        #2진 탐색을 위한 중앙값 pivot설정
        mid_x=(start_x + end_x)//2
        mid_y=(start_y + end_y)//2

        # 경우0
        if A[mid_x] + B[mid_y] == t:
            answer=True
            break
        # 경우1
        elif A[mid_x]+B[mid_y]>t:
            end_x=mid_x-1
        # 경우1 X원소들 불만족 상태-> Y원소 탐색
        elif end_x<start_x and A[mid_x]+B[mid_y]>t:
            end_y=mid_y-1
        # 경우2
        elif start_x<=end_x and A[mid_x]+B[mid_y]<t:
            start_x=mid_x+1
        # 경우2 X원소들 불만족 상태-> Y원소 탐색
        else: #start_x>end_x and A[mid_x]+B[mid_y]<t
            start_y=mid_y+1

        # 경우3
        if mid_x<0 or mid_x>len_x-1 or mid_y<0 or mid_y>len_y-1 or (mid_x==len_x-1 and mid_y==len_y-1) :
            break
    return answer

#A,B,C의 각 리스트 입력 받기 #+3n
A= list(map(int, input().split()))
B= list(map(int, input().split()))
C= list(map(int, input().split()))

#각 리스트 정렬 #+nlogn
A.sort()
B.sort()
C.sort()

#함수를 호출하여 결과 출력
# 알고리즘 결과값 반환용 변수 : A(임의의 원소)+B(임의의 원소)+C(임의의 원소) = 0 만족 전까지 default값 #+1
result=False

# two_sum함수는 'A+B=t'의 값을 찾는 함수이므로 C의 원소들에 '-'로 부호를 바꾸어 +로 t로 대입
for i in C: #*n
    if two_sum(A,B,-i) == True: #*nlogn
        result=True #+1
        break

print(result)
#수행시간 분석 및 Big-O표기
#수행시간 분석: T(n) = 6n^2logn + 3nlogn + 10n +2 (two_sum의 while문을 수행할 때 경우에 따라 정확한 시간복잡도는 다를 수 있을 것 같습니다)
#전체 알고리즘 수행시간 = O(n^2 logn)
