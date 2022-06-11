import sys

# A - Median?
# https://atcoder.jp/contests/abc253/tasks/abc253_a
li = list(map(int, sys.stdin.readline().split()))
li_sorted = sorted(li)
result = "Yes" if li[1] == li_sorted[1] else "No"
print(result)
