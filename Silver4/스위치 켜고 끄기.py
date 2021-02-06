# BOJ 1244 스위치 켜고 끄기
from sys import stdin
SPLITS = 20

def find_symmetric(arr, idx):
    r, l = idx - 1, idx + 1
    min_r, max_l = idx, idx
    while r > 0 and l < len(arr):
        if arr[r] == arr[l]:
            min_r, max_l = r, l
            r -= 1
            l += 1
        else:
            break
    return max(idx - min_r, max_l - idx)


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.insert(0, -1)
n = int(stdin.readline())
for _ in range(n):
    sex, idx = map(int, stdin.readline().split())
    if sex == 1:
        for idx in range(idx, len(arr), idx):
            arr[idx] = (arr[idx] + 1) % 2
    elif sex == 2:
        width = find_symmetric(arr, idx)
        temp = arr[idx-width: idx+width + 1]
        for i in range(len(temp)):
            temp[i] = (temp[i] + 1) % 2
        arr[idx-width:idx+width+1] = temp
for idx in range(1, len(arr), SPLITS):
    print(*arr[idx:idx+SPLITS])
