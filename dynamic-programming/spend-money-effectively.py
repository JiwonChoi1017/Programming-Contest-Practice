import sys

# 効率的な貨幣構成
n, m = map(int, sys.stdin.readline().split())

li = []
for _ in range(n):
    li.append(int(sys.stdin.readline().rstrip()))
li.sort()

d = [10001] * (m + 1)
# 0ウォンの場合、貨幣を1個も使わなかった場合のみ作れるため0にしておく
d[0] = 0

for i in range(n):
    for j in range(li[i], m + 1):
        # 漸化式：
        # ai-kが作れる場合：ai = min(ai, ai-k + 1)
        # ai-kが作れない場合：ai = 10001
        if d[j - li[i]] != 10001:
            d[j] = min(d[j], d[j - li[i]] + 1)

print(d[m] if d[m] != 10001 else -1)
