import copy
import sys

# 冒険者ギルド
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

cnt = 0
li_copy = copy.deepcopy(li)

while len(li_copy) > 0:
    # リストの中で一番恐怖度の高い冒険者
    m = max(li_copy)

    for _ in range(m):
        li_copy.remove(max(li_copy))

    n = n % m
    cnt += 1

print(cnt)
