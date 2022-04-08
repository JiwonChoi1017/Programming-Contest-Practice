import sys

# 1にする
# なんかわけのわからないこーどになっちゃった
x = int(sys.stdin.readline().rstrip())
cnt = 0

while x > 1:
    if x >= 5:
        if x % 5 == 0:
            x //= 5
        else:
            x -= 1

        cnt += 1
        continue

    if x % 3 == 0:
        x //= 3
    elif x % 2 == 0:
        x //= 2
    else:
        x -= 1

    cnt += 1

print(cnt)
