import random #난수를 가지고 있는 package 삽입

n = int(input('난수의 개수를 입력하세요: '))

for _ in range(n):
    r = random.randint(10,99) # random.randint(시작할 수, 끝낼 수 )--> 시작할 수 부터 끝낼 수까지의 난수를 구하라는 수식
    print(r, end=' ')
    if r ==13:
        print('\n프로그램을 중단합니다.')
        break
    
else :       
    print('\n난수 생성을 종료합니다.') 

#만약에 else가 없다면, 모든 순환(for반복문을 통한 모든 순환)에 "난수 생성을 종료합니다." 라는 문자열이 출력된다.
#따라서 else를 반드시 입력해서 for반복이 이루어질 때 (if문이 실행되는 조건)과 구분하여야 한다.
#여기서 알 수 있는 점 -->else는 if없이 단독으로 사용은 불가하지만,  if elif else의 suite가 반복문의 안/밖에 구애 받지 않고 사용이 가능하다. 