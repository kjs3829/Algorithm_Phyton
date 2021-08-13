# Baekjoon 2714 문자를 받은 승환이

import sys

# chr(int(0b00001)+64)
def bin_to_str(bin):
    r = int(bin, 2)+64
    return chr(r) if r != 64 else ' '


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    R, C, text = sys.stdin.readline().rstrip().split()
    R, C = int(R), int(C)
    mat = [[0]*C for _ in range(R)]
    idx = 0
    for r in range(R):
        for c in range(C):
            mat[r][c] = text[idx]
            idx += 1
    result = ''
    r, c, cnt = 0, 0, 0
    rw, lw, tw, bw = C, -1, -1, R
    while len(result) != len(text):
        # 오른쪽
        while c < rw:
            result += mat[r][c]
            c += 1
        tw += 1
        r += 1
        c -= 1
        if len(result) == len(text):
            break
        # 아래
        while r < bw:
            result += mat[r][c]
            r += 1
        rw -= 1
        r -= 1
        c -= 1
        if len(result) == len(text):
            break
        # 왼쪽
        while c > lw:
            result += mat[r][c]
            c -= 1
        bw -= 1
        c += 1
        r -= 1
        if len(result) == len(text):
            break
        # 위
        while r > tw:
            result += mat[r][c]
            r -= 1
        lw += 1
        r += 1
        c += 1
    start_idx = 0
    rs = ''

    for _ in range(len(result)//5):
        rs += bin_to_str('0b' + result[start_idx:start_idx+5])
        start_idx += 5

    if len(result) % 5 != 0:
        rs += bin_to_str(result[start_idx+1:len(result)] + '0'*(5-(len(result) % 5)))
    rs.rstrip()
    print(rs.rstrip())
