import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

# 진입차수와 그래프 초기화
indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

# 입력 데이터를 바탕으로 그래프 구성 및 진입차수 계산 
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        result.append(x)

        for nx in graph[x]:
            indegree[nx] -= 1
            if indegree[nx] == 0:
                q.append(nx)

    print(*result)

topology()