import sys

# B - Takahashi's Failure
# https://atcoder.jp/contests/abc252/tasks/abc252_b
n, k = map(int, sys.stdin.readline().split())
foods = list(map(int, sys.stdin.readline().split()))
dislike_foods = list(map(int, sys.stdin.readline().split()))

first_eat = [i + 1 for i, x in enumerate(foods) if x == max(foods)]

is_dislike_food = [i for i in first_eat if i in dislike_foods]

print("Yes" if len(is_dislike_food) > 0 else "No")
