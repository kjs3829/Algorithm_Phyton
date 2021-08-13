# Baekjoon 1063 킹

import sys

def move(m, k):
    result = k.copy()
    if m == 'B':  result[0] += 1
    elif m == 'T': result[0] -= 1
    elif m == 'L': result[1] -= 1
    elif m == 'R': result[1] += 1
    elif m == 'LT':
        result[0] -= 1
        result[1] -= 1
    elif m == 'LB':
        result[0] += 1
        result[1] -= 1
    elif m == 'RT':
        result[0] -= 1
        result[1] += 1
    elif m == 'RB':
        result[0] += 1
        result[1] += 1
    return result


K, S, N = map(str, sys.stdin.readline().rstrip().split())
K = [8 - int(K[1]), ord(K[0]) - 65]   # ord(A) = 65
S = [8 - int(S[1]), ord(S[0]) - 65]   # [y, x]

for _ in range(int(N)):
    m = sys.stdin.readline().rstrip()
    tmpK = move(m, K)
    tmpS = S.copy()

    # 돌의 위치에 킹이 갔을경우 돌을 이동시킴
    if tmpK == tmpS:
        tmpS = move(m, tmpS)

    if -1 < tmpK[0] < 8 and -1 < tmpK[1] < 8 and -1 < tmpS[0] < 8 and -1 < tmpS[1] < 8:
        K, S = tmpK, tmpS

print(chr(K[1] + 65) + str(8 - K[0]))
print(chr(S[1] + 65) + str(8 - S[0]))
