import random
from max import max_of

print('난수의 최댓값을 구합니다.')
num = int(input('난수의 개수를 입력하세요.: '))
lo = int(input('난수의 최솟값을 입력하세요.: '))
hi = int(input('난수의 최댓값을 입력하세요.: '))
x = [None]*num #원소의 갯수가 num 개 라는 의미

for i in range(num):
    x[i] = random.randint(lo, hi) #배열 x의 num개의 원소 중 i 번째 의 원소를 random.randint를 이용하여 변경한다는 의미

print(f'{(x)}') #배열 내의 원소들을 출력한다는 의미
print(f'이 가운데 최댓값은 {max_of(x)}입니다.') #배열 가운데 최댓값을 출력