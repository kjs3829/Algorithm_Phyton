# BOJ 1072 게임
# 이분탐색
# 'Z = Y / X * 100'과 같이 계산한 덕분에 한시간을 삽질했다.
# X, Y의 범위가 굉장히 넓기 때문에 메모리 관련 문제가 발생할 수도 있다고한다.
# 'Z = 100 * Y / X'와 같이 계산해 주면 해결된다.
import sys

X, Y = map(int, sys.stdin.readline().split())
Z = 100 * Y / X
left = 0
right = 1000000000
result = -1
findR = int(Z+1)

while Z < 99 and left <= right:
    mid = (left + right) // 2
    win_rate = 100 * (Y + mid) / (X + mid)
    if findR < win_rate:
        right = mid - 1
        if 100 * (Y + right) / (X + right) < findR:
            result = mid
            break
    elif findR > win_rate:
        left = mid + 1
        if 100 * (Y + left) / (X + left) >= findR:
            result = left
            break
    else:
        result = mid
        break

print(result)
