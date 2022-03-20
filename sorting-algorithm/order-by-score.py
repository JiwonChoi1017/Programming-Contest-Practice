import sys


# 成績順にデータの並び替え
def compare_score(item):
    return int(item[1])


n = int(sys.stdin.readline())
li = []
for _ in range(n):
    li.append(tuple(sys.stdin.readline().split()))

li.sort(key=compare_score)

for i in li:
    print(i[0], end=" ")
