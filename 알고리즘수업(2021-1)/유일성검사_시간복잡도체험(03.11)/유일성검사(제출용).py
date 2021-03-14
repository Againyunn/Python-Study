import random, time

def unique_n(A):#O(n^2)
	# code
	answer="*"#답을 출력할 변수 Answer 지정
	for i in range(len(A)):
		for j in range(len(A)):
			if i!=j:
				if A[i]==A[j]: # list A 안에 동일한 원소가 한쌍이라도 존재할 경우 -> No 저장
					answer="No"
			else: #list A 내의 모든 원소가 다를 경우 -> Yes 저장
				answer="Yes"
	return answer #결과값 출력
	
def unique_nlogn(A):#O(nlogn)
	# code
	answer="Yes"#answer의 기본값은 Yes로 지정
	A.sort() #nlogn 의 big-O 복잡도 이미 생성
	for i in range(len(A)): # 각 원소 수만큼의 i를 호출
		if i < len(A)-1:
			if A[i]==A[i+1]:
				answer="No"
		else:
			break
	return answer

def unique_n(A): #O(n)
	# code
	B=[] #A의 원소를 저장할 새로운 list B생성
	answer="Yes"#기본 answer 값은 Yes로 설정
	for i in A: # i!=B인 경우(중복 원소가 없는 경우)
		if i != B:
			B.append(i)
		else: #i==B 인 경우(중복 원소가 있는 경우)
			answer="No" #중복 원소가 1개라도 존재하는 경우엔 No로 answer의 변수 변경
	return answer
		
	
# input: 값의 개수 n
n = int(input('측정할 n의 값을 입력하시오: '))
# -n과 n 사이의 서로 다른 값 n 개를 랜덤 선택해 A 구성
A = random.sample(range(-n, n+1), n)

###########시간측정###########
s1=time.process_time()
result1= unique_n(A)
e1= time.process_time()

s2=time.process_time()
result2= unique_nlogn(A)
e2= time.process_time()

s3=time.process_time()
result3= unique_n(A)
e3= time.process_time()

time1=(e1-s1)+10000
time2=(e2-s2)+10000
time3=(e3-s3)+10000

print(result1 ,result2, result3)
print('<수행시간>')
print('unique_n(A) = ',time1)
print('unique_nlogn(A) = ', time2)
print('unique_n(A) = ', time3)

# 위의 세 개의 함수를 차례대로 불러 결과 값 출력해본다
# 당연히 모두 다르게 sample했으므로 YES가 세 번 연속 출력되어야 한다
# 동시에 각 함수의 실행 시간을 측정해본다
# 이러한 과정을 n을 100부터 10만까지 다양하게 변화시키면서 측정한다


#측정시간 기록:
#10 입력 시
#unique_n(A) =
#unique_nlogn(A) =
#unique_n(A) =




