import sys

# 王室のナイト
a = sys.stdin.readline()
d = ["a", "b", "c", "d", "e", "f", "g", "h"]

b = int(d.index(a[0]) + 1)
c = int(a[1])

cnt = 0

for i in range(c - 2, c + 3):
    if i == c:
        continue

    if (c - i) % 2 == 0 and 0 < i < 8:
        if 0 < b - 1 < 8:
            cnt += 1

        if 0 < b + 1 < 8:
            cnt += 1

    if (c - i) % 2 == 1 and 0 < i < 8:
        if 0 < b - 2 < 8:
            cnt += 1

        if 0 < b + 2 < 8:
            cnt += 1

print(cnt)
