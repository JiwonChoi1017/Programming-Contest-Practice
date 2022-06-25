import sys

# A - A to Z String 2
# https://atcoder.jp/contests/abc257/tasks/abc257_a
n, x = map(int, sys.stdin.readline().split())
alphabet_str = "".join([chr(i) * n for i in range(65, 91)])

print(alphabet_str[x - 1])
