def max3(a,b,c): #함수 선언
    maximum= a
    if b>maximum: 
        maximum=b
    if c>maximum:
        maximum=c
    return maximum #함수의 반환 값 설정 : 함수를 선언한 뒤 유의미한 연산을 하기 위해 설정 필요

print(f'max3(3,2,1)={max3(3,2,1)}')
print(f'max3(3,2,2)={max3(3,2,1)}')
print(f'max3(3,1,2)={max3(3,2,1)}')
print(f'max3(3,2,3)={max3(3,2,1)}')
