import sys

# タイル工事
n = int(sys.stdin.readline().rstrip())
d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    # 漸化式：ai = ai-1 + ai-2 * 2
    d[i] = (d[i - 1] + d[i - 2] * 2) % 796796

print(d[n])
