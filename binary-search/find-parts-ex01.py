import sys


# パーツ探し（二分探索）
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None


n = int(sys.stdin.readline().rstrip())
n_list = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().rstrip())
m_list = list(map(int, sys.stdin.readline().split()))

n_list.sort()

for i in m_list:
    result = binary_search(n_list, i, 0, n - 1)
    print("yes" if result is not None else "no", end=" ")
