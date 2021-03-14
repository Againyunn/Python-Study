import sys

def solution():
    asw=input('문제별 정답을 입력하시오: ').split() #정답 입력
    score=input('문제별 배점을 입력하시오: ').split() #배점 입력
    num_Paper=int(input("제출한 답안지의 갯수를 입력하시오: ")) #제출한 답안지 수 
    
    #제출한 답안지 n갯수 만큼 리스트 생성
    mod = sys.modules[__name__]
    for n in range(1, num_Paper+1):
        i=int(input('문제지 별 입력한 답을 기입하시오: ')) #변수i로 답안을 입력받아 제출한 답안지 submit[]에 저장
        setattr(mod, 'submit{}'.format(n), i)
    
    result[i]=[] #맞춘 문제의 수 기록
    num_Test=len(asw) #문제의 문항수
    
    '''for j in range(num_Paper)
        for i in range(num_Test):
            if asw[i]==submit[i]: #정답이 맞은 문제 문항을 기록
                result.append(i)'''
                


    answer=print(f'정답을 맞춘 문제: {result}번 입니다.')
    return answer

if __name__=="__main__":
    sol=solution()
    print(sol)


    
    