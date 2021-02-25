print('세 정수의 최댓값 구하기')
a= int(input('정수 a의 값을 입력하세요.')) #형 변환 : 일반적으로 input함수는 문자열로서 데이터를 입력받는다. 따라서 정수 데이터를 변수에 담기 위해 int()로 형 변환
b= int(input('정수 b의 값을 입력하세요.'))
c= int(input('정수 c의 값을 입력하세요.'))

maximum = a
if b> maximum : 
    maximum=b
if c> maximum :
    maximum=c

print(f'최댓값은 {maximum}입니다.') # print(f'문자열{} 문자열')은 {}안의 변수를 문자열 사이에 출력한다.

#순차구조 : 1~6행까지 / 일반적인 코드로서 한 줄씩 실행되는 구조
#선택구조 : 7~10행까지 / 조건식 처럼 프로그램의 실행 흐름이 바뀌는 구조




