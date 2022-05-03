import sys

# 掛け算もしくは足し算
s = sys.stdin.readline().rstrip()
result = int(s[0])

for idx in range(1, len(s)):
    number = int(s[idx])
    if number <= 1 or result <= 1:
        result += number
    else:
        result *= number

print(result)
