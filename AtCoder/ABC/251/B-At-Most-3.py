import itertools
import sys

# B - At Most 3 (Judge ver.)
# https://atcoder.jp/contests/abc251/tasks/abc251_b
n, w = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
result = []

for i in range(1, 4):
    # 重複を許容しない
    sum_a = [sum(i) for i in list(itertools.combinations(a, i)) if sum(i) <= w]
    result.append(sum_a)

# ２次元のリストを平坦化
result = set(itertools.chain.from_iterable(result))

print(len(result))
