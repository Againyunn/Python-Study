global BLANK, end_of_array, end_of_temp_array

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

temp = [0] * n
BLANK = 0
end_of_array = n
end_of_temp_array = 0

task1_s, task1_e = tuple(map(int, input().split()))
task2_s, task2_e = tuple(map(int, input().split()))

# #task 반영 함수
# def do_task(start, end):
#     for i in range(start, end):
#         arr[i] = 0

# #젠가 빼기 함수
# def remove_block():
#     global end_of_array, end_of_temp_array

#     for i in range(end_of_array):
#         if arr[i] != BLANK:
#             temp[end_of_temp_array] = arr[i]
#             end_of_temp_array += 1

#     for i in range(end_of_temp_array):
#         arr[i] = temp[i]
    
#     end_of_array = end_of_temp_array

#task1 실행
for i in range(task1_s, task1_e):
    arr[i] = BLANK

for i in range(end_of_array):
    if arr[i] != BLANK:
        temp[end_of_temp_array] = arr[i]
        end_of_temp_array += 1

arr = []
for i in range(end_of_temp_array):
    arr.append(temp[i])

end_of_array = end_of_temp_array

temp = [0] * end_of_array
end_of_temp_array = 0

#task2 실행
for i in range(task2_s, task2_e):
    arr[i] = BLANK

for i in range(end_of_array):
    if arr[i] != BLANK:
        temp[end_of_temp_array] = arr[i]
        end_of_temp_array += 1

arr = []
for i in range(end_of_temp_array):
    arr.append(temp[i])

end_of_array = end_of_temp_array

#결과 출력
if end_of_array == 0:
    print(0)
else:
    for i in arr:
        print(i)


#문제 해설1
# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
def cut_array(start_idx, end_idx):
    global end_of_array, numbers
    
    temp_arr = []
    
    # 구간 외의 부분만 temp 배열에 순서대로 저장합니다.
    for i in range(end_of_array):
        if i < start_idx or i > end_idx:
            temp_arr.append(numbers[i])

    # temp 배열을 다시 numbers 배열로 옮겨줍니다.
    end_of_array = len(temp_arr)
    for i in range(end_of_array):    
        numbers[i] = temp_arr[i]


# 두 번에 걸쳐 지우는 과정을 반복합니다.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을 삭제합니다.
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])

#파이썬의 전역변수 개념정리
'''
mutable -> 전역변수 필요x
immutable -> 전역변수 필요o

mutable도 새롭게 선언할 때는 전역변수 필요(지역변수로 인식한다)
수정만 전역변수 없이 가능

단, mutable/immutable 에 관계 없이 값을 조회하는 것은 전역변수 없이 가능하다.
'''

#문제해설2
# 변수 선언 및 입력
n = int(input())
numbers = [
    int(input())
    for _ in range(n)
]
end_of_array = n


# 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
def cut_array(start_idx, end_idx):
    global end_of_array
    
    cut_len = end_idx - start_idx + 1
    for i in range(end_idx + 1, end_of_array):
        numbers[i - cut_len] = numbers[i]
    
    end_of_array -= cut_len


# 두 번에 걸쳐 지우는 과정을 반복합니다.
for _ in range(2):
    s, e = tuple(map(int, input().split()))
    # [s, e] 구간을 삭제합니다.
    cut_array(s - 1, e - 1)

# 출력:
print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])
