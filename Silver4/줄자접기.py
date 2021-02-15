# BOJ 2597 줄자접기
# 구현
from sys import stdin
cm = int(stdin.readline())
fold = 0
dots = []
for i in range(3):
    a, b = map(int, stdin.readline().split())
    dots.append(a)
    dots.append(b)

for i in range(0, len(dots), 2):
    l, s = max(dots[i], dots[i+1]), min(dots[i], dots[i+1])
    if l == s:
        continue
    fold = ((l-s)/2)+s
    if cm - fold > fold:
        for j in range(len(dots)):
            if dots[j] < fold:
                dots[j] = fold + fold - dots[j]
        for j in range(len(dots)):
            dots[j] -= fold
        cm = cm - fold
    else:
        for j in range(len(dots)):
            if dots[j] > fold:
                dots[j] = fold - (dots[j] - fold)
        cm = fold
print('%.1f'%cm)

