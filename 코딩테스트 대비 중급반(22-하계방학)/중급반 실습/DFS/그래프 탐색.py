N, M = tuple(map(int, input().split()))

start_points = []
end_points = []
for i in range(M):
    s_num, e_num = tuple(map(int, input().split()))
    start_points.append(s_num)
    end_points.append(e_num)

VERTICES_NUM = N
# EDGES_NEM = 6

graph = [
    [0 for _ in range(VERTICES_NUM + 1)]
    for _ in range(VERTICES_NUM + 1)
]

visited = [False for _ in range(VERTICES_NUM + 1)]
global result
result = 0

def dfs(vertex):
    global result
    for curr_v in range(1, VERTICES_NUM + 1):
        if graph[vertex][curr_v] and not visited[curr_v]:
            # print(curr_v)
            result += 1
            visited[curr_v] = True
            dfs(curr_v)



for start, end in zip(start_points, end_points):
    graph[start][end] = 1
    graph[end][start] = 1

root_vertex = 1
# print(root_vertex)
visited[root_vertex] = True
dfs(root_vertex)

print(result)

