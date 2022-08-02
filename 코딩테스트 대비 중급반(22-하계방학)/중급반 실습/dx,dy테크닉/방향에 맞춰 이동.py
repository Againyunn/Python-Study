num = int(input())

x, y = 0, 0
direction = ['N','S','E','W']
'''
단순 리스트 대신 dictionary 사용하면 더 효율적!
    dir_map = {
        "N":0,
        "S":1,
        "E":2,
        "W":3
    }
'''

move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]

# list의 원소 크기에 따라 반복문 외부와 내부에 선언할 지를 정해야 한다.
# ex) 원소 크기가 100개 미만일 때는 반복문 내부에 선언해도 큰 의미가 없지만, 1000을 넘어가는 많은 원소를 가진 경우 반복량 * 원소 수 만큼의 비효율이 발생

'''
for문에서 i를 직접 사용하지 않는 경우 python에서는 i대신 _사용한다.
    for _ in range(num):    
'''
for i in range(num):
    this_direction, this_move = tuple(input().split())
    this_move = int(this_move)
    tmp = direction.index(this_direction)
    x += this_move * move_x[tmp]
    y += this_move * move_y[tmp]

print(f"{x} {y}")

# dx, dy 테크닉은 일반적으로 list자료형을 사용한다.

'''
    특정문자 == 인덱스의 규칙을 가진 경우
    ASCII코드의 기법을 활용해서 임의의 ASCII코드로 만들어서 사용할 수도 있다.
'''

'''
    map으로 객체를 변형할 경우 결과 값의 자료형은 map이다.
    따라서 tuple, list 처럼 unpacking할 수 있는 자료형으로 바꾸는 게 좋다
'''