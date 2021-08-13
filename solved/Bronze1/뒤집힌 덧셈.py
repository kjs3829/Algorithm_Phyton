# Baekjoon 1357 뒤집힌 덧셈

X, Y = input().split()
rx, ry, a = "", "", ""
for x in range(len(X)):
    rx += X[-(x+1)]
for y in range(len(Y)):
    ry += Y[-(y+1)]
result = int(rx) + int(ry)
result = str(result)
for r in range(len(result)):
    a += result[-(r+1)]
print(int(a))
