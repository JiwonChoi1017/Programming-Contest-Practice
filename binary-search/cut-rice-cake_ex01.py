import sys

# トッポギ用の餅切り
n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(n_list)

result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for i in n_list:
        if i > mid:
            total += i - mid
    if total < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)
