# BOJ 5397 키로거
# 자료 구조, 스택
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    password = input().rstrip()
    left, right = [], []
    for i in password:
        if i == "<":
            if left:
                right.append(left.pop())
        elif i == ">":
            if right:
                left.append(right.pop())
        elif i == "-":
            if left:
                left.pop()
        else:
            left.append(i)
    if right:
        print(''.join(left) + ''.join(reversed(right)))
    else:
        print(''.join(left))
