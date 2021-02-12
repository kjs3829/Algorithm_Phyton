# BOJ 9012 괄호
from sys import stdin
for i in range(int(stdin.readline())):
    vps = list(stdin.readline().rstrip())
    while vps:
        idx = -1
        for j in range(len(vps)):
            if vps[j] == ')':
                idx = j
                break
        if idx - 1 < 0:
            break
        else:
            vps.remove(')')
            vps.remove('(')
    if vps:
        print("NO")
    else:
        print("YES")



