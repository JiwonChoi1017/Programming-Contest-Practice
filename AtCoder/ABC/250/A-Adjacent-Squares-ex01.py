# A - Adjacent Squares
# https://atcoder.jp/contests/abc250/tasks/abc250_a
h, w = map(int, input().split())
r, c = map(int, input().split())
# booleanをintに変換し、その合計を取得
s = sum(map(int, [r == 1, c == 1, r == h, c == w]))
# 最大値から合計をひく
print(4 - s)
