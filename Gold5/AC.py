# BOJ 5430 AC
# 자료 구조, 덱
# 출력되는 값의 띄어쓰기 때문에 계속 틀린 문제
# 출력 형식을 자세히 보자
import sys
from collections import deque
input = sys.stdin.readline


def AC(p, x):
    delete = True   # True일 때 popleft, False일 때 popright
    for i in p:
        if i == 'R':
            delete = not delete
        else:
            if x:
                if delete:
                    x.popleft()
                else:
                    x.pop()
            else:
                return "error"
    if not delete:
        x.reverse()
    return '[' + ','.join(list(x)) + ']'


for _ in range(int(input())):
    p = input().rstrip()
    n = int(input())
    x = input().rstrip()[1:-1].split(',')
    x = deque([]) if n == 0 else deque(list(x))
    print(AC(p, x))
