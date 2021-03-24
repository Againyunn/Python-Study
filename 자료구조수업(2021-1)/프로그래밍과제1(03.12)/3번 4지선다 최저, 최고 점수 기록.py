# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
	asw=input().split() #정답 입력
	score=input().split() #배점 입력
	num_Paper=int(input()) #제출한 답안지 수 
	submit=[None]*num_Paper#제출한 답안지의 빈 2차 배열 list x 문제지 갯수

	for i in range(num_Paper):
		submit[i]=input().split() #변수i로 답안을 입력받아 제출한 답안지 submit[]에 저장
		submit[i]=list(map(int,submit[i]))
	#list들의 데이터 형태를 integer로 변경
	asw=list(map(int,asw))
	score=list(map(int,score))
    
	result=[0]*num_Paper #맞춘 문제의 수 기록
	num_Test=len(asw) #문제의 문항수
	for i in range(num_Test): #i= 문제의 문항번호 측정
		for k in range(num_Paper): #문제지 번호 측정용
			if submit[k][i] == asw[i]: #각 문제지 별로 답이 맞는 지 확인
				result[k]+=1*score[i] #맞은 문제별 배점을 고려한 점수 기록
				result=list(map(int,result))

	winner_Score=max(result)
	worst_Score=min(result)
	
	return worst_Score , winner_Score 

#함수 실행코드
sol1,sol2=solution()
print(sol1,sol2)
