import sys

# 作れない金額
n = int(sys.stdin.readline().rstrip())
li = list(map(int, sys.stdin.readline().split()))
li.sort()

result = 1

for i in li:
    if result < i:
        break
    # result未満の金額が作れるという意味である。
    result += i

print(result)
