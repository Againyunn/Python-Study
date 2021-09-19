def reverse_ver1(A):
    n, i = len(A), 0
    while i < (n-1):
        A[i], A[n-1] = A[n-1], A[i]
        i += 1
        n -=1

def reverse_ver2(A):
    n, i = len(A), 0
    while i < (n-1)//2:
        A[i], A[n-1-i] = A[n-1-i], A[i]
        i += 1

#내가 만든 버전:
A = list(input())  # 문자열을 입력받아 리스트로 변환
tmp=list(A) #리스트를 복사할 때엔 바로 = 을 이용하면 에러 발생(기존의 리스트와 함께 바뀐다)
reverse_ver1(A)
print(''.join(str(x) for x in A))

#성주(실습)버전:
A=tmp
reverse_ver1(A)
print(''.join(str(x) for x in A))