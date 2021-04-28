#딕셔너리 선언
d={'과목1':'자료구조','과목2':'컴논개'}

#삽입
d['과목3']='데이터구조'
d['과목4']='컴개실'
print(d)

#ADT 활용 예시
Get=d.get('과목1')
Show=d.values()
KeysList=list(d.keys())
ValuesList=list(d.values())
Tuple_d=d.items()
print(f' Get={Get} \n Show={Show} \n KeysList={KeysList} \n ValuesList={ValuesList} \n Tuple_d={Tuple_d}')

print()
#집합 선언
s={0,1,2}

s.add(4)
s.update([10,6])
s.remove(0)
length=len(s)

t={0,1,2,20}
Union=s.union(t)
Intersection=s.intersection(t)
Difference=s.difference(t)

print(f'집합 : {s} \nUnion : {Union} \nIntersection : {Intersection} \nDifference : {Difference}')


#comprehension
a = []
for x in range(31):
    if x % 3 ==0:
        a.append(x)

#a=[x for in range(31) if x%3==0]


def add(*args):
    sum=0
    for x in args:
        sum+=x
    return sum
print(add(3,4,5,6))


def say_myself(name, old, man=True):
    print("나의 이름은 %s 입니다" %name)
    print("나이는 %d 살 입니다." %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")


def increase1(x):
    x +=1

x=10
increase1(x)
print(x)

s=[]
s.append(3)
s.extend('4')
s.extend({5:6, 7:8})
print(s)

aa=s.copy()
print(aa,"\n")
string= "hello world"
tu=(1,2,3,4)
print(max(string))
print(max(tu))