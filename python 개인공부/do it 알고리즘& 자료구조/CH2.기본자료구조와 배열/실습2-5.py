from max import max_of

t = (4,7,5.6,2,3,3.14, 1)
s = 'string'
a = ['DTS' , 'AAC' , 'FLAX']

print(f'{t}의 최댓값은  {max_of(t)} 입니다.')
print(f'{s}의 최댓값은 {max_of(s)} 입니다.') #string이라는 문자열 중 사전 순으로 가장 큰 문자 값인 t를 출력합니다.
print(f'{a}의 최댓값은 {max_of(a)} 입니다.') #사전 순으로 가장 큰 문자 값인 FLAX를 출력한다.