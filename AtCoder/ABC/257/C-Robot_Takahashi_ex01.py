import sys

# C - Robot Takahashi
# https://atcoder.jp/contests/abc257/tasks/abc257_c
n = int(sys.stdin.readline().rstrip())
s = [int(i) for i in sys.stdin.readline().rstrip()]
w = [int(x) for x in sys.stdin.readline().split()]
h = [(a, b) for a, b in zip(w, s)]

# 重さ順にソート
h.sort()

ans = sum(s)
m = ans

for i, (a, b) in enumerate(h):
    # ｘがa以下の場合は子供、aより大きい場合は大人。
    if b == 1:
        m -= 1
    else:
        m += 1
    if i < n - 1:
        # 同じ値が入っている場合は比較しない
        if a != h[i + 1][0]:
            ans = max(ans, m)
    else:
        ans = max(ans, m)

print(ans)
