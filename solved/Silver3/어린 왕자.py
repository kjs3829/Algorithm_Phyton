# BOJ 1004 어린왕자
# 기하학
import sys
import math

for _ in range(int(sys.stdin.readline())):
    start_dot = list(map(int, sys.stdin.readline().split()))    # [x1,y1,x2,y2]
    cnt = 0
    for _ in range(int(sys.stdin.readline())):
        circle = list(map(int, sys.stdin.readline().split()))   # [x,y,round]
        dist_sc = math.sqrt((start_dot[0]-circle[0])**2 + (start_dot[1] - circle[1])**2)
        dist_ec = math.sqrt((start_dot[2] - circle[0]) ** 2 + (start_dot[3] - circle[1]) ** 2)

        # 출발점과 도착점이 같은 원안에 있지 않을 경우
        if (dist_sc > circle[2] >= dist_ec) or (dist_sc <= circle[2] < dist_ec):
            cnt += 1
    print(cnt)
