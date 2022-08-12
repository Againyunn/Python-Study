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
		#return self.items.pop() 
		if self.isEmpty():
			answer='fail'
			return answer #비었다고 표시 error 처리를 위해 0으로 반환하도록 설정
		else:
			try:
				return self.items.pop() #items에서 삭제 후 반환
			except IndexError:
				nswer='fail'
				return answer #비었다고 표시 error 처리를 위해 0으로 반환하도록 설정
		def size(self):
			return len(self.items)
		###테스트 목적 : 리스트 출력
		#def tt(self): 
		#return self.items

def evalPostfix(expr):
	#print(expr)
	s = Stack()
	parenthesis = ['+','-','*','//']  
	for token in expr:
		#print(s.tt())
		if token in parenthesis:
			#print(token)
			val2 = s.pop()
			try:
				val1=s.pop()
			except ValueError:
				val1='fail'
				if val1=='fail':
					answer='error'
					return answer
				#print(f'val1 : {val1} , val2 : {val2}')
				if (token =='+'): 
						s.push(val1+val2)
				elif (token =='-'):
						s.push(val1-val2)
				elif (token =='*'):
						s.push(val1 * val2)
				elif (token =='//'):
						s.push(val1 // val2)
		else: # ; 을 입력받은 경우
			if token==';':
				t1=int(s.pop())#연산자로 계산된 마지막 피연산자 값 pop
				#t2=s.pop()
				if s.pop()=='fail':
					answer=t1
				if s.pop()!='fail': #연산을 모두 했음에도 불구하고 피연산자가 스택에 남은 경우
					answer='error'
				return answer
			s.push(float(token))

if __name__=='main':
    expr=input()
    sol=evalPostfix(expr)
    print(sol)