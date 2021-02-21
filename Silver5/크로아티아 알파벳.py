# BOJ 2941 크로아티아 알파벳
from sys import stdin

c = ['c-', 'c=', 'dz=', 'd-', 'lj', 'nj', 'z=', 's=']
string = stdin.readline().rstrip()

for t in c:
    string = string.replace(t, '*')

print(len(string))
