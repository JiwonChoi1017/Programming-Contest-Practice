import sys

# 降順ソート
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(int(sys.stdin.readline()))
li.sort(reverse=True)

print(" ".join(map(str, li)))
