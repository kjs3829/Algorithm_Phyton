# BOJ 1181 단어 정렬
# 정렬
import sys

voca_list = []
N = int(sys.stdin.readline())
for i in range(N):
    voca_list.append(sys.stdin.readline().rstrip())
set_voca_list = list(set(voca_list))
sort_voca_list = []
for j in set_voca_list:
    sort_voca_list.append((len(j), j))
sort_voca_list.sort()
for len_voca, voca in sort_voca_list:
    print(voca)
