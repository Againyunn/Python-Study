a, b = map(int, input().split())

r=a
decimals=[]

if a < b:
    answer1=0
    i=0
    while(i<20):
        q = (r * 10) // b
        r = (r * 10) % b
        decimals
