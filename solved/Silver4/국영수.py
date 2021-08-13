# BOJ 10825 국영수
from sys import stdin

n=int(stdin.readline())
a=[]

for i in range(n):
    a.append(stdin.readline().split())

a.sort(key =lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(a[i][0])