def gcd_sub(a, b):
    while a * b != 0:
        if a>b:
            a = a-b
        else:
            b = b-a
    return a+b

def gcd_mod(a, b):
    while a * b != 0:
        if a>b:
            a = a%b
        else:
            b = b%a
    return a+b


def gcd_rec(a, b):
    if a*b ==0:
        return a + b
    if a>b:
        return gcd_rec(a-b, b)
    else:
        return gcd_rec(a, b-a)

def gcd_rec2(a, b): #성주 풀이(조교)
    if a<b:
        tmp=a
        a=b
        b=tmp

    if b<=0:
        return a
    else:
        return gcd_rec2(a-b, b)


# a, b를 입력받는다
# gcd_sub, gcd_mod, gcd_rec을 각각 호출하여, x, y, z에 리턴값을 저장한다
a, b = input().split(" ")
a = int(a)
b = int(b)

x = gcd_sub(a, b)
y = gcd_mod(a, b)
z = gcd_rec(a, b)
zz = gcd_rec2(a, b)

print(x, y, z, zz)