# Baekjoon 1002 터렛

import sys
import math

T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        dist = math.sqrt((x2-x1)**2 +(y2-y1)**2)
        largeR = r1 if r1 > r2 else r2
        smallR = r1 if largeR != r1 else r2
        if largeR > dist:
            if dist+smallR == largeR:
                print(1)
            elif dist+smallR < largeR:
                print(0)
            else:
                print(2)
        elif largeR == dist:
            print(2)
        else:
            if r1+r2 == dist:
                print(1)
            elif r1+r2 < dist:
                print(0)
            else:
                print(2)
