# Baekjoon 1110 더하기 사이클

N = int(input())

a = N//10 + N%10
new = N%10*10+(a%10)
cnt=1

while new != N:
    a = new // 10 + new % 10
    new = new % 10 * 10 + (a % 10)
    cnt+=1

print(cnt)
