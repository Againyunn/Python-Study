area = int(input('직사각형의 넓이를 입력하세요.: '))

for i in range(1, area+1):
    if i * i > area : #i*i가 area(넓이)보다 커지면 순환 중지
        break
    if area % i:  #나머지가 존재하면 값을 추가하여 계속 순환
        continue
    print(f'{i}*{area//i}')