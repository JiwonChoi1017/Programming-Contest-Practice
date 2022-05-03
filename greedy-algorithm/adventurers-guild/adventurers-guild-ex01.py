import sys

# 冒険者ギルド
n = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))
# リストを昇順にソート
li.sort()

re = 0
# 冒険者数
cnt = 0

for i in li:
    cnt += 1
    # 現在ギルドに参加した冒険者数が現在の恐怖度が多い（高い？）場合
    if cnt >= i:
        re += 1
        cnt = 0

print(re)
