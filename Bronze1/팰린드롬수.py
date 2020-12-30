# Baekjoon 1259 팰린드롬수

result_set = []
while 1:
    n = int(input())
    if n == 0:
        break
    result_set.append(str(n))

for n in result_set:
    l_idx = 0
    r_idx = -1
    flag = False
    while l_idx < len(n)//2:
        if n[l_idx] != n[r_idx]:
            flag = True
            print("no")
            break
        l_idx += 1
        r_idx -= 1
    if not flag:
        print("yes")
