import copy
import sys
from collections import deque


# カリキュラム
def topological_sort():
    # 深いコピー
    result = copy.deepcopy(hours)
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + hours[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n + 1):
        print(result[i])


n = int(sys.stdin.readline())

hours = [0] * (n + 1)
indegree = [0] * (n + 1)
graph = [[] for i in range(n + 1)]

for i in range(1, n + 1):
    a = list(map(int, sys.stdin.readline().split()))
    hours[i] = a[0]
    for j in a[1:-1]:
        indegree[i] += 1
        graph[j].append(i)

topological_sort()
