import re


def solution(new_id):

    # 1단계
    tmp = new_id.lower()

    # 2단계
    id = ''
    for c in tmp:
        if 'a' <= c <= 'z' or '0' <= c <= '9' or c == '-' or c == '_' or c =='.':
            id += c

    # 3단계
    r = re.compile('[..]+')
    id = r.sub('.', id)

    # 4단계
    if len(id) > 1:
        if id[0] == '.':
            id = id[1:]
        elif id[-1] == '.':
            id = id[:-1]
    if id == '.':
        id = ''

    # 5단계
    if len(id) == 0:
        id = 'a'

    # 6단계
    if len(id) > 15:
        id = id[:15]
    if len(id) > 1:
        if id[0] == '.':
            id = id[1:]
        elif id[-1] == '.':
            id = id[:-1]
    if id == '.':
        id = ''

    # 7단계
    if len(id) <= 2:
        id += id[-1] * (3 - len(id))

    return id
