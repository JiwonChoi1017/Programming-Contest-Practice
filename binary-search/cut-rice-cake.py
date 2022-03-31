import sys


# トッポギ用の餅切り
def find_max_length(max_length):
    global n
    global m
    global n_list

    rice_cake = 0
    for i in n_list:
        rice_cake += i - max_length if i >= max_length else 0

    if rice_cake == m:
        return max_length

    # 餅切り器の高さの上限が１０億のため、線形探索だと実行時間超過エラーになるはず
    return find_max_length(max_length - 1)


n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))

max_length = find_max_length(max(n_list))

print(max_length)
