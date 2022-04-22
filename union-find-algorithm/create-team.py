import sys


# チーム結成
def find_parent(parent, x):
    print("find_parent", parent[x], x)
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return x


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    print("union_parent", a, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    print("parent", parent)


n, m = map(int, sys.stdin.readline().split())

parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

result = []

for _ in range(m):
    s, a, b = map(int, sys.stdin.readline().split())
    if s == 0:
        union_parent(parent, a, b)
    else:
        result.append("YES" if parent[a] == parent[b] else "NO")

for i in result:
    print(i)
