import sys

# 成績順にデータの並び替え
n = int(sys.stdin.readline())
li = []
for _ in range(n):
    data = sys.stdin.readline().split()
    li.append((data[0], int(data[1])))

li = sorted(li, key=lambda student: student[1])

for i in li:
    print(i[0], end=" ")
