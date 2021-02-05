# BOJ 1439 뒤집기
# 그리디
from sys import stdin

s = stdin.readline()
change = []
for i in range(1, len(s)):
    if s[i - 1] != s[i]:
        change.append(i)
isOdd = False
if len(change) % 2 == 1:
    isOdd = True

result = len(change) // 2
if isOdd:
    result += 1
print(result)
