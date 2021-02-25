# 날짜(YYYY M D)와 문제 번호 두개(p1 p2)를 입력하면 readme.md를 업데이트 시켜준다.
# 날짜에 'today'를 입력하면 현재 날자를 적용시킨다.
from datetime import datetime
import re


def sentence(qlist):
    sb = ''
    for i in range(len(qlist)):
        sb += '<br />[BOJ ' + qlist[i] + '](https://www.acmicpc.net/problem/' + qlist[i] + ')'
    return sb


# UserInterface
n = input("Enter YYYY M D to edit README.md : ").split()
y, m, d = 0, 0, 0
if n[0] == 'today':
    y, m, d = datetime.today().year, datetime.today().month, datetime.today().day
else:
    y, m, d = n[0], n[1], n[2]
ql = list(input("Enter question numbers : ").split())
flag = False
buffer = ''

# Service
with open("README.md", 'r+', encoding='utf-8') as fin:
    data = fin.readlines()
    p = re.compile('\*\*' + str(d) + '[^\|]*')
    for line in data:
        if line == '<!--' + str(y) + ' ' + str(m) + '-->\n':
            flag = True
        if flag:
            if line == '</p>\n':
                flag = False
            buffer += p.sub('**' + str(d) + '**' + sentence(ql), line)
            # - old version
            # 이미 작성된 날짜는 update가 불가능한 코드
            # buffer += line.replace('**' + str(d) + '**', '**' + str(d) + '**' + sentence(p1, p2))
        else:
            buffer += line
with open("README.md", 'w+', encoding='utf-8') as f:
    f.write(buffer)

