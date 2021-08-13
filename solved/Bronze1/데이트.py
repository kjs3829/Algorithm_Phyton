# Baekjoon 1296 데이트

p = input()
num = int(input())
old_percent = -1
old_name = ""
result = ""
pL = p.count("L")
pO = p.count("O")
pV = p.count("V")
pE = p.count("E")
for x in range(num):
    name = input()
    L = name.count("L") + pL
    O = name.count("O") + pO
    V = name.count("V") + pV
    E = name.count("E") + pE

    if (((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100) > old_percent:
        old_percent = ((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100
        old_name = name
        result = name
    elif (((L+O)*(L+V)*(L+E)*(O+V)*(O+E)*(V+E)) % 100) == old_percent:
        if name < old_name:
            old_name = name
            result = name
print(result)



