def solution(s):
    if len(s)==4 or len(s)==6:
        try:
            if int(s)//1 >=0:
                return True
        except ValueError:
            return False
    else:
        return False


if __name__ == '__main__':
    while True:
        s= input('수를 입력하세요.')
        if 1<=len(s)<=8:
            break
    
    a= solution(s)
    print(a)
#소요시간 : 15분~ 20분? 가량 소요되었습니다.