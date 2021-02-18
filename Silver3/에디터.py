# BOJ 1406 에디터
# 자료구조, 스택
from sys import stdin

string = list(stdin.readline().rstrip())
stack = []
for _ in range(int(stdin.readline())):
    a = stdin.readline().rstrip().split()
    if a[0] == 'L' and string:
        stack.append(string.pop())
    if a[0] == 'D' and stack:
        string.append(stack.pop())
    if a[0] == 'B' and string:
        string.pop()
    if a[0] == 'P':
        string.append(a[1])
print(''.join(string + list(reversed(stack))))
