# Baekjoon 1292 쉽게 푸는 문제

import sys

number_list = []
for i in range(1, 46):
    number_list += [i] * i

A, B = map(int, sys.stdin.readline().split())
print(sum(number_list[A - 1:B]))
