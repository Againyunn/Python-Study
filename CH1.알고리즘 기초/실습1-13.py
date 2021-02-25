print('+와 -를 번갈아 출력합니다.')
n=int(input('몇 개를 출력할까요?: '))

for _ in range(n//2): #입력 받은 수의 몫의 갯수만큼 +-를 반복한다는 의미 
    print('+-', end='') 
    # for _ in range() 에서 _로 처리 한 이유 --> python에서는 무시할 값을 _로서 처리하여 pass 시킬 수 있다.
 
if n%2: #몫의 갯수만큼 +-를 출력하고 n이 홀수일 경우 마지막에 +를 출력한다는 의미
    print('+', end='')

print()