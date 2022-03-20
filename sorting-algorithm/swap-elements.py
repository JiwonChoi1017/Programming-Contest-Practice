import sys

# リストの要素を交換
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

for _ in range(k):
    # aの最小値を取得
    min_a = min(a)
    min_a_idx = a.index(min_a)
    # bの最大値を取得
    max_b = max(b)
    max_b_idx = b.index(max_b)

    # 要素の入れ替え
    if min_a <= max_b:
        a[min_a_idx], b[max_b_idx] = b[max_b_idx], a[min_a_idx]

print(sum(a))
