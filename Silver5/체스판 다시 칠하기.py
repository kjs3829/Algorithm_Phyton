# Baekjoon 1018 체스판 다시 칠하기

N, M = map(int, input().split())
B1 = ["WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"]
B2 = ["BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"]
mat = [input() for x in range(N)]
old_cnt1, old_cnt2 = 65, 65

for x in range(M-7):
    for y in range(N-7):
        cnt1, cnt2 = 0, 0
        for ix in range(8):
            for iy in range(8):
                if mat[iy+y][ix+x] != B1[iy][ix]:
                    cnt1 += 1
                if mat[iy+y][ix+x] != B2[iy][ix]:
                    cnt2 += 1
        if cnt1 < old_cnt1:
            old_cnt1 = cnt1
        if cnt2 < old_cnt2:
            old_cnt2 = cnt2

print(old_cnt1) if old_cnt1 < old_cnt2 else print(old_cnt2)
