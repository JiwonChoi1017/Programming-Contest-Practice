import re
import sys

# 文字列反転
s = sys.stdin.readline().rstrip()
li_zero = re.findall("0+", s)
li_one = re.findall("1+", s)

print(min(len(li_zero), len(li_one)))
