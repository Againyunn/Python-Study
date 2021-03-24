def solution():
	pb=input()#입력 받은 문자열
	pb=pb.lower()#입력받은 문자열의 대/소문자를 '소문자' 형식으로 통일
	pb=list(pb)
	result=[]#회문의 부회문들을 담을 리스트
	
	for i in pb: #각 원소들을 result에 저장
		##동일 원소가 1개인 경우
		if pb.count(i)==1:
			result.append(i) #1개인 원소들 먼저 result에 저장 
			pb.remove(i)#result에 저장된 원소는 pb에서 삭제


		if pb.count(i)>1: #리스트 내에 원소가 2개 이상 등장한 경우
			result.append(i)
			pb.remove(i)#result에 저장된 원소는 pb에서 삭제

			for a in result: #결과 값의 적용
				if i== a: # result에 i와 동일한 값이 저장되어 있는 경우 -> 회문여부 체크를 위한 전제 조건
					n=i#회문 여부 체크를 위한 임의의 변수 n
					num=pb.index(i) #i의 pb원소 번호를 담는 변수

					try:
						for k in range(num+1,len(pb)): #현 원소보다 뒤의 원소들에서 추가
							n+=pb[k]
							rn=n[::-1] #n의 값을 뒤집기
							if n==rn and not(): #n으로 추가한 값이 회문일 때
								#회문의 각 원소가 하나로만 구성된 경우는 추가x
								ln=list(n) #n이 같은 원소들로만 구성되어 있는 지 판단하기 위해 임시로 list변형하여 저장한 값ln
								for f in ln:#ln의 원소 출력
									if ln.count(f)==len(ln): #n에 담은 부회문이 모두 같은 원소인 경우
										break
									else:
										#회문의 각 원소가 다를경우
										result.append(n)#새로 만들어낸 부회문을 result에 추가
										n=list(n)
										for j in n: #논리 체크 필요 -> n에 사용된 원소를 pb에서 제거
											pb.remove(j)
										break
					except IndexError:
						for k in range(num+1,len(pb)-1): #현 원소보다 뒤의 원소들에서 추가
							n+=pb[k]
							rn=n[::-1] #n의 값을 뒤집기
							if n==rn and not(): #n으로 추가한 값이 회문일 때
								#회문의 각 원소가 하나로만 구성된 경우는 추가x
								ln=list(n) #n이 같은 원소들로만 구성되어 있는 지 판단하기 위해 임시로 list변형하여 저장한 값ln
								for f in ln:#ln의 원소 출력
									if ln.count(f)==len(ln): #n에 담은 부회문이 모두 같은 원소인 경우
										break
									else:
										#회문의 각 원소가 다를경우
										result.append(n)#새로 만들어낸 부회문을 result에 추가
										n=list(n)
										for j in n: #논리 체크 필요 -> n에 사용된 원소를 pb에서 제거
											pb.remove(j)
										break
						
		else: #pb에 원소 하나가 남은 경우
			new_pb=pb
			while True:
				if new_pb!=[]:
					for l in new_pb:
						result.append(l) #1개인 원소들 먼저 result에 저장 
						pb.remove(l)#result에 저장된 원소는 pb에서 삭제
				else:
					break

	answer=sorted(set(result))#사전 순으로 배열
	return answer

sol= solution()
print(' '.join(sol))
