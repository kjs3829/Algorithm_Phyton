# BOJ 10866 덱
from sys import stdin

q = []
for i in range(int(stdin.readline())):
    c = stdin.readline().rstrip()
    if " " in c:
        a, b = c.split()
        if a == 'push_front':
            q.insert(0, b)
        elif a == 'push_back':
            q.append(b)
    elif "pop_front" == c:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(0))
    elif "pop_back" == c:
        if len(q) == 0:
            print(-1)
        else:
            print(q.pop(-1))

    elif 'size' == c:
        print(len(q))
    elif 'empty' == c:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'front' == c:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    elif 'back' == c:
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
