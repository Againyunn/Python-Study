# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
	n1=input()
	n1=n1.lower()#입력받은 문자열의 대/소문자를 '소문자' 형식으로 통일
	n2=list(n1) #문자열의 대/소문자 통일 후 list 형태로 n2에 저장
	r_n=n2[::-1] #list명[::-1] 명령어를 통해 손쉽게 list내의 배열 변경가능(reverse와 같은 기능 수행)

	check=0 #일치하는 문자열 확인
	answer="*"#결과
	for i in range(len(n2)):
		if n2[i]==r_n[i]: #회문 전 원소 vs 회문 후 원소 비교
			check+=1 
	if check==len(n2): #모든 원소(회문 전, 후)가 check(일치)하는 지 확인  
		answer="yes"
	else: #하나라도 다를 경우
		answer="no"
	return answer

#함수 실행 코드
sol= solution()
print(sol)