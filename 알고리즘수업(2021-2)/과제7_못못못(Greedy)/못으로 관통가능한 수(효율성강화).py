# def stick_num(stick, n):
#     result=[]
#     index=0
#     # stick.sort()
#
#     while index< n-1:
#         check_f = stick[index][0]
#         check_l = stick[index][1]
#         tmp = 0
#
#         print(f'check_f={check_f}')
#         print(f'check_l={check_l}')
#
#         for i in range(n):
#             # if 조건문 조절 필요
#             # if (check_f <= stick[i][0] and stick[i][1] <= check_l) or (check_f==stick[i][1] and check_l==stick[i][0]):
#                 tmp+=1
#                 print(f'stick[{i}][0]={stick[i][0]}')
#                 print(f'stick[{i}][1]={stick[i][1]}')
#
#         result.append(tmp)
#         index+=1
#
#     return max(result)

# def stick_num(stick, n):
#     result=0
#     index=0
#
#     while index< n-1:
#         tmp1 =0
#         tmp2 =0
#
#         for i in range(n):
#             check1= stick[i][0]
#             check2= stick[i][1]
#             if check1 <= stick[index][0] and stick[index][0] <= check2:
#                 tmp1+=1
#             if check1 <= stick[index][1] and stick[index][1] <= check2:
#                 tmp2+=1
#
#         result = max(result, tmp1, tmp2)
#         index += 1
#
#     return result

# def stick_num(stick, n):
#     result=0
#     index=0
#     stick.sort()
#     max_index=max(stick, key=stick.count)
#     # print(max_index)
#
#     for a in range(len(max_index)):
#         tmp=0
#         for i in range(n):
#             if stick[i][0]<= stick[a][1] and stick[a][1] <= stick[i][1]:
#                 tmp+=1
#         result = max(result, tmp)
#     return result


    # while index< n-1:
    #     tmp1 =0
    #
    #     for i in range(n):
    #         check1= stick[i][0]
    #         check2= stick[i][1]
    #         if check1 <= stick[index][1] and stick[index][1] <= check2:
    #             tmp1+=1
    #
    #     result = max(result, tmp1)
    #     index += 1
    #
    # return result

def stick_num(stick, n):
    stick.sort(key=lambda time: time[1])  # 길이가 짧은 막대의 순서대로 오름차순 배열 O(n log n)
    result =0

    for i in range(0,n):
        check = stick[i][1]
        tmp=0
        j=i
        for j in range(i,n):
            if stick[j][0] <= check and check <= stick[j][1]:
                tmp+=1
            else:
                break
        result = max(result, tmp)

    return result
n=int(input())
stick=[]
for i in range(n):
    stick.append(list(map(int, input().split())))

print(stick_num(stick, n))