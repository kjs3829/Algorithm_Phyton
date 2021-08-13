# BOJ 5525 IOIOI
# 문자열
from sys import stdin
N = int(stdin.readline())
M = int(stdin.readline())
S = stdin.readline().rstrip()

answer = 0
pattern = 0
i = 1
while i < M - 1:
    if S[i - 1] == 'I' and S[i] == 'O' and S[i + 1] == 'I':
        pattern += 1
        if pattern == N:
            pattern -= 1
            answer += 1
        i += 1
    else:
        pattern = 0
    i += 1
print(answer)
