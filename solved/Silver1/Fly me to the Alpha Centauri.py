# BOJ 1011 Fly me to the Alpha Centauri
# 수학
import sys

for _ in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    diff = y - x

    if diff == 1:
        print("1")
    else:
        min_v = 2
        max_v = 2
        cnt = 2
        i = 2
        flag = False
        while 1:
            for _ in range(2):
                if min_v <= diff <= max_v:
                    flag = True
                    break
                min_v = max_v + 1
                max_v += i
                cnt += 1
            i += 1
            if flag:
                print(cnt)
                break

