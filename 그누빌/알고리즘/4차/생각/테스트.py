def solution(info, query):
    queryList = []
    temp_query = []
    result = []

    for q in range(len(query)):
        queryList = query[q].replace('and ', '').split(' ')

    print(queryList)
    answer = result
    return answer

info=input("info : ").split('"')
query=input("query : ").split('"')
sol=solution(info,query)
print(sol)