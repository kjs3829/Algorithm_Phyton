# Beakjoon 1316 그룹 단어 체커

import sys

n = int(sys.stdin.readline())

group_word = 0
for _ in range(n):
    word = sys.stdin.readline()
    error = 0
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0:
                error += 1
    if error == 0:
        group_word += 1
print(group_word)
