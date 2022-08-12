def gcd(a ,b): # a,b 가 양의 정수일 때
#    if(a%b ==0):
#        return b
    if b==0: #base case
        return a
    else:
        return gcd(b, a%b)

print(gcd(120, 50))