# BOJ 1043 거짓말
# 분리 집합, 그래프 이론
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

# 거짓말치면 안되는 사람의 번호를 담는 스택
# 진실을 아는 사람의 수는 필요가 없어 슬라이싱 함
know = list(map(int, input().split()))[1:]

# 스택에 추가된 적이 있는지 확인하기 위한 리스트
visit = [0] * N
for k in know:
    visit[k-1] = 1

parties = []
for _ in range(M):
    guests = list(map(int, input().split()))[1:]    # 파티 손님의 수는 필요가 없어 슬라이싱 함
    parties.append(guests)

party_visit = [0] * M   # 방문 결과가 0이면 거짓말을 한 파티, 1이면 진실을 말한 파티

while know:
    known_guest = know.pop()

    candidate = set()   # 진실을 아는 사람과 알게 될 사람들의 번호를 저장하는 집합

    for party_idx in range(len(parties)):
        party = set(parties[party_idx])
        if known_guest in party:    # 진실을 알고 있는 사람이 현재 파티에 있을 경우
            candidate = candidate.union(party)  # 진실을 아는 사람과 알게 될 사람들의 번호를 저장
            party_visit[party_idx] = 1  # 현재 파티를 진실을 말한 파티로 설정

    for guest in candidate:
        if not visit[guest - 1]:
            know.append(guest)  # 거짓말치면 안되는 사람의 번호를 담는 스택에 추가된 적이 없으면 스택에 추가
            visit[guest - 1] = 1

print(party_visit.count(0))
