# Baekjoon 2607 비슷한 단어

import sys

N = int(sys.stdin.readline().rstrip())
compare = list(input())
ans = 0
for _ in range(N-1):
    compare_word = compare[:]
    check_word = list(sys.stdin.readline())
    for _ in range(len(check_word)):
        a = check_word.pop(0)
        if a in compare_word:
            compare_word.remove(a)
        else:
            check_word.append(a)
    A = len(compare_word)
    B = len(check_word)
    if (A == 0 and B == 0) or (A == 1 and B == 0) or (A == 0 and B == 1) or (A == 1 and B == 1):
        ans += 1
print(ans)
