def calculation():
    while True:
        i = input('입력값 : ')
        if i =='end':
            return True
        else:
            i=int(i)
            if i%3>0:
                print(i)
            
            else :
                print('짝')

if __name__=="__main__":
    cal=calculation()
    print(cal)
