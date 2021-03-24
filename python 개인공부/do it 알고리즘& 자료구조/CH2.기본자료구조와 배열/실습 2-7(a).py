def cord_conv(x: int , r: int) -> str:
    d=''
    dchar= '0123456789ABCDEFGHIJKLMNOPQRSTUWXYZ'

    while x>0:
        d +=dchar[x % r] # 해당하는 문자를 꺼내어 결합처리
        x //=r

        return d[::-1] #역순으로 반환