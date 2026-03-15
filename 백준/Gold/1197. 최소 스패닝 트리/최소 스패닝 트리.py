import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a != b:
        if rank[a] < rank[b]:
            parent[a] = b
        elif rank[a] > rank[b]:
            parent[b] = a
        else:
            parent[b] = a
            rank[a] += 1


def kruskal(v, edges):
    parent = [i for i in range(v + 1)]
    rank = [0] * (v + 1)

    edges.sort()

    mst_weight = 0
    mst_edges = 0

    for weight, a, b in edges:
        if find(parent, a) != find(parent, b):
            union(parent, rank, a, b)
            mst_weight += weight
            mst_edges += 1

            if mst_edges == v - 1:
                break

    return mst_weight


V, E = map(int, input().split())

edges = []
for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

print(kruskal(V, edges))