def solution():
	n1=input()
	n1=n1.lower()#입력받은 문자열의 대/소문자를 '소문자' 형식으로 통일
	n2=list(n1) #문자열의 대/소문자 통일 후 list 형태로 n2에 저장
	r_n=n2[::-1] #list명[::-1] 명령어를 통해 손쉽게 list내의 배열 변경가능(reverse와 같은 기능 수행)

	check=0 #일치하는 문자열 확인
	answer="*"#결과
	#checkList=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']#모든 문자열 나열
	result=[]#회문의 부회문들을 담을 리스트
	for i in range(len(n2)):
		if n2[i]==r_n[i]: #회문 전 원소 vs 회문 후 원소 비교
			check+=1 
	#if check==len(n2): #모든 원소(회문 전, 후)가 check(일치)한다면 회문이므로 연산시작
	for i in range(len(n1)): #각 원소들을 result에 저장
		for j in range(i):# 0<j <i : i보다 j가 작아서, i 이전의 값이 result에 존재하는 지 확인하는 용도로 사용
			if i==0:#첫번째 원소일 때
				result.append(n1[0]) #result에 원소 추가
			if 0<i<len(n1): #중간 원소일 때, j가 i보다 작은 경우(i보다 앞의 원소 번호를 갖는 경우)
				while True: #앞의 원소들과 중복되는 값이 있는 경우-> 반복하지 않을 때까지 반복
					n=n1[i]#임의의 값: 앞에 이미 있는 원소들과 중복되는 값을 추가
					if n1[j]!=n1[i]: #앞의 원소들과 중복되는 원소가 없다면 result에 저장
						result.append(n1[i])
						break#if문 탈출
					else: #앞의 원소에 중복되는 원소가 있는 경우
						for k in range(i+1,len(n1)): #현 원소보다 뒤의 원소들에서 추가
							n+=n1[k]
							rn=n[::-1] #n의 값을 뒤집기
							if n==rn : #n으로 추가한 값이 회문일 때
								result.append(n)#새로 만들어낸 부회문을 result에 추가
								break #for문 탈출
						break#else문 탈출
	#사전순으로 배열하여 출력
	answer=sorted(set(result))#사전 순으로 배열

	return answer


sol= solution()
print(' '.join(sol))