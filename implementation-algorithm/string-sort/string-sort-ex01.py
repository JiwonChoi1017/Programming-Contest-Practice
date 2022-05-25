import sys

# 文字列ソード
s = sys.stdin.readline().rstrip()
result = []
value = 0

for i in s:
    # isalpha()： 文字列中のすべての文字（大文字・小文字）が英字で、かつ1文字以上ある場合にtrueを返す
    if i.isalpha():
        result.append(i)
    else:
        value += int(i)

result.sort()

if value > 0:
    result.append(str(value))

print("".join(result))
