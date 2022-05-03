import sys

# 掛け算もしくは足し算
s = sys.stdin.readline().rstrip()
# 0を掛けると0になってしまう、かつ足しても結果に影響がないため除外する
s = s.replace("0", "")
result = int(s[0])

for idx in range(1, len(s)):
    number = int(s[idx])
    if number > 1:
        result *= number
    else:
        result += number

print(result)
