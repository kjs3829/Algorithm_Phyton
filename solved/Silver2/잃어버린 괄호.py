# BOJ 1541 잃어버린 괄호
from sys import stdin

s = stdin.readline().rstrip().split('-')
a = list(map(int, s[0].split('+')))
result = sum(a)
for i in range(1, len(s)):
    a = list(map(int, s[i].split('+')))
    tmp = sum(a)
    result -= tmp
print(result)
