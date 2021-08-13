# Baekjoon 1059 좋은 구간

L = int(input())
S = list(map(int, input().split()))
n = int(input())
S.sort()
isExist = False
left = 1
for idx in range(len(S)):
    if S[idx] == n:
        isExist = True
        break
    elif S[idx] > n:
        right = S[idx]-1
        break
    left = S[idx]+1

if isExist:
    print("0")
else:
    print((right-n+1)*(n-left)+right-n)
