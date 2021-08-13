# Baekjoon 1157 단어 공부

N = input().upper()
# ASCII A=65, Z=90
A = 65
alpabet = [0]*26

for x in N:
    alpabet[ord(x)-A] += 1
biggest = max(alpabet)
if alpabet.count(biggest) >= 2:
    print('?')
else:
    print(chr(A+alpabet.index(biggest)))
