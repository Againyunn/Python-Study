# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
	asw=input().split() #정답 입력
	score=input().split() #배점 입력
	submit=input().split() #제출한 답안지 입력

	num=len(asw) #문제의 문항수
	result=[] #맞춘 문제의 수 기록
	for i in range(num):
		if asw[i]==submit[i]: #정답이 맞은 문제 문항을 기록
			result.append(i)
		
	result=list(map(int, result))
	score=list(map(int,score))
	
	right_score=0#맞춘 점수를 기록할 변수	
	for i in range(len(result)):
		n=result[i]#맞은 문항 번호를 입력받을 변수 
		right_score+= score[n] #맞은 문항의 배점을 right_score에 추가
	
	return right_score

#함수 실행코드
sol=solution()
print(sol)