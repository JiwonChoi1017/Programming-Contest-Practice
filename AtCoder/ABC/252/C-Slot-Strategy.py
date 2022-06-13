import collections
import sys

# C - Slot Strategy
# https://atcoder.jp/contests/abc252/tasks/abc252_c
n = int(sys.stdin.readline().rstrip())
s_list = [sys.stdin.readline().rstrip() for _ in range(n)]

answer = 10 * n

for i in range(10):
    time = [x.index(str(i)) for x in s_list]
    new_time = [k if v == 1 else k + 10 * (v - 1) for k, v in collections.Counter(time).items()]
    answer = max(new_time) if answer > max(new_time) else answer

print(answer)