# Baekjoon 1252 이진수 덧셈

A, B = map(str, input().split())

if len(A) < len(B):
    A = A.zfill(len(B))
else:
    B = B.zfill(len(A))

result = ["0"]*(len(A)+1)
carry, nC = 0, 0

for idx in range(-1, -(len(A)+1), -1):
    carry = 1 if nC else 0
    R = (int(A[idx])+int(B[idx])+carry) % 2
    nC = 1 if int(A[idx])+int(B[idx])+carry > 1 else 0
    result[idx] = str(R)

if nC:
    result[0] = "1"

result = "".join(result)
sidx = result.find("1")
if sidx == -1:
    print(0)
else:
    print(result[sidx:])
