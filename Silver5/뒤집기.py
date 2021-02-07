# BOJ 1439 뒤집기
# 그리디
from sys import stdin

S = stdin.readline().rstrip()
m = '0' if S.count('0') < S.count('1') else '1'
cnt1 = 0
c = S[0]
cnt2 = 0
for i in range(1, len(S)):
    if S[i] != c and S[i] == '0':
        cnt1 += 1
    elif S[i] != c and S[i] == '1':
        cnt2 += 1
    c = S[i]
if S[-1] == '1':
    cnt1 += 1
else:
    cnt2 += 1
print(cnt1) if cnt1 < cnt2 else print(cnt2)


