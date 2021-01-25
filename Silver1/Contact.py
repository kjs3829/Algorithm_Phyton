# BOJ 1013 Contact
# 문자열
import sys
import re

# Use RE
for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    p = re.compile('(100+1+|01)+')
    m = p.fullmatch(s)
    if m:
        print("YES")
    else:
        print("NO")

