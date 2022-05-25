import re
import sys

# 文字列ソード
s = sys.stdin.readline().rstrip()

int_list = list(map(int, re.findall(r"\d", s)))
re_str = "".join(sorted(re.findall(r"\D", s)))

print(re_str, sum(int_list), sep="")
