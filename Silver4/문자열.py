# BOJ 1120 문자열
# 문자열
import sys

A, B = sys.stdin.readline().split()
for start_idx in range(len(B)-len(A) + 1):
    cnt = 0
    for idx in range(len(A)):
        if A[idx] != B[idx+start_idx]:
            cnt += 1
    result = min(result, cnt) if start_idx != 0 else cnt
print(result)
