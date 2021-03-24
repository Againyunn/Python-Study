print('2자리 양수를 입력하세요.')

while True:
    n = int(input('숫자를 입력하세요.'))
    if 10<=n and n<=99: #드모르간의 법칙
        break
print(f'입력받은 숫자는 {n}입니다.')