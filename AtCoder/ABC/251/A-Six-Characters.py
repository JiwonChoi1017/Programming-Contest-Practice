import sys

# A - Six Characters
# https://atcoder.jp/contests/abc251/tasks/abc251_a
s = sys.stdin.readline().rstrip()
loop_cnt = 6 // len(s)

print(s * loop_cnt)
