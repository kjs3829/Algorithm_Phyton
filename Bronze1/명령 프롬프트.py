# Baekjon 1032 명령프롬프트

N = int(input())
l = [input() for _ in range(N)]
result = ''

for n in range(len(l[0])):
    v = l[0][n]
    flag = True
    for idx in range(1, len(l)):
        if v != l[idx][n]:
            flag = False
            break
    if not flag:
        result += '?'
    else:
        result += v

print(result)


