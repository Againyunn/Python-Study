class Stack:
	def __init__ (self):
		self.items=[]
	def isEmpty(self):
		return len(self.items) == 0
	def clear(self):
		self.items=[]
	def push(self,e):
		self.items.append(e)
	def pop(self):
		if self.isEmpty():
			return True #비었다고 표시
		else:
			try:
				return self.items.pop() #items에서 삭제 후 반환
			except IndexError:
				return True #비었다고 표시
	def size(self):
		return len(self.items)
    ###테스트 목적 : 리스트 출력
    #def tt(self): 
    #    return self.items

def parenthsesBalance(string):
	s=Stack()
	openParenthesis = '({['
	closeParenthesis = ']})'
	success=str(1)
	fail=str(0)
	error=['error1','error2','error3','error4','error5','error6']
	checkNum=0
	checkIndex=[0]*len(string)
	#print(checkIndex)
	for k in range(len(string)):
		checkIndex[k]=[0,0]
	
	for i in range(len(string)): 
		ch=string[i]
		n=str(i)
		checkIndex[i][0]=n
		checkIndex[i][1]=ch
		#print(f'순서: {i} ,ch : {ch}')
		if ch in openParenthesis: #ch가 여는 괄호 중 하나인 경우
			s.push(ch)
			#checkIndex.append(i)
		elif ch in closeParenthesis: #ch가 '공백'이거나 '닫는 괄호 중 하나'인 경우
			num=str(i)
			if s.isEmpty()==True: #스택이 비어있는 경우
				if ch =='(':
					return num ,str(error[3])
				elif ch =='{':
					return num ,str(error[4])
				elif ch =='[':
					return num ,str(error[5])
				elif ch ==')':
					return num, str(error[0])
				elif ch =='}':
					return num, str(error[1])
				elif ch ==']':
					return num, str(error[2])
				
			else: #스택이 비어있지 않은 경우
				openCh=s.pop()
				for j in range(len(string)):
					print(checkIndex[j][1])
					print(checkIndex)	
					if checkIndex[j][1]==openCh:
						del checkIndex[j][0]
						del checkIndex[j][0]
					print(checkIndex)		
				#del checkIndex[len(checkIndex)-1] #가장 최근에 추가된 값을 제거
			
				#print(f'openCh : {openCh}')
				if ch==')' and openCh !='(' :
					return num ,str(error[0])
				elif ch=='}' and openCh !='{':
					return num ,str(error[1])
				elif ch ==']' and openCh !='[' :
					return num , str(error[2])
				'''elif ch =='' and i==len(string)-1:
					if openCh =='(':
						return num ,str(error[3])
					elif openCh =='{':
						return num ,str(error[4])
					elif openCh =='[':
						return num ,str(error[5])
						#print(s.tt())'''
				if i==len(string)-1:
					if s.isEmpty()!=True:
						openCh=s.pop()
						for i in range(len(checkIndex)):
							if checkIndex[i][1]==openCh:
								num=checkIndex[i][0]
								break
						if openCh =='(':
							return num ,str(error[3])
						elif openCh =='{':
							return num ,str(error[4])
						elif openCh =='[':
							return num ,str(error[5])
						elif openCh ==')':
							return num, str(error[0])
						elif openCh =='}':
							return num, str(error[1])
						elif openCh ==']':
							return num, str(error[2])
			
string=input()
sol=parenthsesBalance(string)
print(' '.join(sol))
#print(sol)
