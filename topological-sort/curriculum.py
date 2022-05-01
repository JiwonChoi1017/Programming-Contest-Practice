import sys
from collections import deque


# カリキュラム
# parent探しは不要かも？
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def topological_sort():
    q = deque()
    result = []

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        s = hours[now]

        for i in m[now]:
            s += hours[i]

            if find_parent(parent, now) != find_parent(parent, i):
                union_parent(parent, now, i)

            if 1 not in m[now]:
                s += hours[parent[now]]

        result.append(s)

        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i)


n = int(sys.stdin.readline())

parent = [0] * (n + 1)
hours = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]
m = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    parent[i] = i

for i in range(1, n + 1):
    a = list(map(int, sys.stdin.readline().split()))
    hours[i] = a[0]
    indegree[i] += len(a[1:-1])
    m[i] = a[1:-1]
    for j in a[1:-1]:
        graph[j].append(i)

topological_sort()
