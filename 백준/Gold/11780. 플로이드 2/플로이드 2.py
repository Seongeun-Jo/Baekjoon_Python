import sys
input = sys.stdin.readline
INF = 10**9

N,M = int(input()),int(input())

graph = [[INF]*(N+1) for i in range(N+1)]
path = [[[i] for i in range(N+1)] for i in range(N+1)]
for i in range(M):
  x,y,w = map(int,input().split())
  graph[x][y] = min(graph[x][y],w)

for k in range(1,N+1):
  for i in range(1,N+1):
    for j in range(1,N+1):
      if i == j:
        continue
      if graph[i][j] > graph[i][k]+graph[k][j]:
        graph[i][j] = graph[i][k]+graph[k][j]
        path[i][j] = path[i][k]+path[k][j]

for i in range(1,N+1):
  for j in range(1,N+1):
    if graph[i][j] == INF:
      print(0,end=" ")
    else:
      print(graph[i][j],end=" ")
  print()

for i in range(1,N+1):
  for j in range(1,N+1):
    if graph[i][j] == INF:
      print(0)
    else:
      print(len(path[i][j])+1,i,*path[i][j])