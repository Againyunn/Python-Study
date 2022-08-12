#String 데이터 형태의 특성 : 불변

String = 'Aasfd'
String.lower()
print(String)

'''
출력 시 결과 값:
    Aasfd
'''






#클래스 주요 내용 정리1
class Car:
    def __init__(self, color,speed,gear): #Car 클래스가 다룰 주요 데이터(클래스 속성)
        self.color=color
        self.speed=speed
        self.gear=gear
    def speedUp(self,s): #speedUp 메소드의 인자로 s를 입력 받음, Car 클래스의 데이터를 인자로 받으므로 self 도 인자로 입력
        self.speed+=s
    def speedDown(self,s): #speedDown 메소드의 인자로 s를 입력 받음, Car 클래스의 데이터를 인자로 받으므로 self 도 인자로 입력
        self.speed-=s
    def getColor(self): #Car 클래스의 데이터를 반환하므로 self만을 인자로 가진다.
        return self.color
    def getSpeed(self): #Car 클래스의 데이터를 반환하므로 self만을 인자로 가진다.
        return self.speed
    def getGear(self): #Car 클래스의 데이터를 반환하므로 self만을 인자로 가진다.
        return self.gear

#클래스 주요 내용 정리2
class Calculation:
    count=0 #모든 Calculation 클래스가 공유하는 공통의 데이터(매개변수)
    def __init__(self, num=0): #num은 Calculation클래스의 default 매개변수
        self.result=num # num(default 매개변수)의 현재 값을 저장하는 클래스 Calculation의 변수
    def clear(self):
        self.result=0


#함수 호출 예시
mycar= Car('red',20,1)
mycar.getColor() #인자가 없는 메소드이므로 ()로 호출
mycar.speedDown(1) #인자 s로서 1을 입력