# 날자(YYYY M D)와 문제 번호 두개(p1 p2)를 입력하면 readme.md를 업데이트 시켜준다.

def sentence(p1, p2):
    return '<br />[BOJ '+ p1 + '](https://www.acmicpc.net/problem/' + p1 + ')<br />[BOJ ' + p2 + '](https://www.acmicpc.net/problem/' + p2 + ')'


n = input("Enter YYYY M D to edit README.md : ").split()
p1, p2 = input("Enter the number of problem1 problem2 : ").split()
flag = False
buffer = ''
with open("README.md", 'r+', encoding='utf-8') as fin:
    data = fin.readlines()
    for line in data:
        if line == '<!--' + n[0] + ' ' + n[1] + '-->\n':
            flag = True
        if flag:
            if line == '</p>\n':
                flag = False
            buffer += line.replace('**' + n[2] + '**', '**' + n[2] + '**' + sentence(p1, p2))
        else:
            buffer += line
with open("README.md", 'w+', encoding='utf-8') as f:
    f.write(buffer)

