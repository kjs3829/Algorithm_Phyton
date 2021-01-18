# Baekjoon 1064 평행사변형

import sys
import math

input = sys.stdin.readline
dots = list(map(int, input().split()))
if (dots[1]-dots[3])*(dots[0]-dots[4]) == (dots[1]-dots[5])*(dots[0]-dots[2]):
    print(-1.0)
else:
    ab = math.sqrt((dots[0] - dots[2])**2 + (dots[1] - dots[3])**2)
    ac = math.sqrt((dots[0] - dots[4])**2 + (dots[1] - dots[5])**2)
    bc = math.sqrt((dots[2] - dots[4])**2 + (dots[3] - dots[5])**2)
    print(max(ab+ac, ab+bc, ac+bc)*2 - min(ab+ac, ab+bc, ac+bc)*2)

