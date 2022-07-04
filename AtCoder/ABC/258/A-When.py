import sys

# A - When?
# https://atcoder.jp/contests/abc258/tasks/abc258_a
k = int(sys.stdin.readline().rstrip())
h = k // 60 + 21
m = k % 60
print("{}:{}".format(h, str(m).zfill(2)))
