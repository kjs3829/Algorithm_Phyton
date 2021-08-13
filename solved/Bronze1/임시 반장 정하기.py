# Baekjoon 1268 임시 반장 정하기

n = int(input())
mat = [input().split() for x in range(n)]
result_set = []
for x in range(n):
    tmp = []
    result_set.append(tmp)

for num in range(n):
    for grade in range(5):
        comp = mat[num][grade]
        for y in range(n):
            if num == y:
                continue
            if comp == mat[y][grade]:
                result_set[num].append(y)
l, idx = -1, 0
for x in result_set:
    if len(list(set(x))) > l:
        l = len(list(set(x)))
        result = idx+1
    idx += 1
print(result)



