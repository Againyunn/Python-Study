print('오른쪽 아래가 직각이등변인 삼각형 출력')
n=int(input('밑변의 길이를 입력하세요.'))

for i in range(n): #각 행을 제어
    b= (n-1)-i #각 행별 빈칸의 갯수 
    print(' '*b,end='')
    for j in range(i+1): #행의 열을 제어
        print('*',end='')
    print()