import sys


# パーツ探し
def binary_search(target, start, end):
    if start > end:
        return "no"
    global n_list

    mid = (start + end) // 2

    if n_list[mid] == target:
        return "yes"

    if n_list[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)


n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()
m_list.sort()

for i in m_list:
    print(binary_search(i, 0, n - 1), end=" ")
