# BOJ 1065 한수
# 브루트포스
import sys

N = sys.stdin.readline().rstrip()
if len(N) < 3:
    print(N)
else:
    cnt = 99
    for x in range(100, int(N)+1):
        isOneN = True
        x = str(x)
        for idx in range(len(x) - 2):
            if int(x[idx]) - int(x[idx + 1]) != int(x[idx + 1]) - int(x[idx + 2]):
                isOneN = False
                break
        if isOneN:
            cnt += 1
    print(cnt)

