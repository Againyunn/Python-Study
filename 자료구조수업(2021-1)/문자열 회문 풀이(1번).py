def solution():
    n1=input("회문 측정할 문자열을 입력하시오: ")
    n1=n1.lower()#입력받은 문자열의 대/소문자를 '소문자' 형식으로 통일
    n2=list(n1) #문자열의 대/소문자 통일 후 list 형태로 n2에 저장
    r_n=n2[::-1] #list명[::-1] 명령어를 통해 손쉽게 list내의 배열 변경가능

    check=0 #일치하는 문자열 확인
    answer="*"#결과
    for i in range(len(n2)):
        if n2[i]==r_n[i]: #회문 전 원소 vs 회문 후 원소 비교
            check+=1 
    if check==len(n2): #모든 원소(회문 전, 후)가 check(일치)하는 지 확인  
        answer="yes"
    else:
        answer="No"
    return answer

if __name__=="__main__":
    sol= solution()
    print(sol)
