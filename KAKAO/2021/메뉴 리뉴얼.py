from itertools import combinations


def solution(orders, course):
    answer = []
    sorted_orders = orders

    for idx in range(len(sorted_orders)):
        sorted_orders[idx] = "".join(sorted(list(sorted_orders[idx])))

    comb_dict = {}
    for i in range(len(course)):
        for order in orders:
            for c in combinations(order, course[i]):
                if c in comb_dict:
                    comb_dict[c] += 1
                else:
                    comb_dict[c] = 1

        max_value = max(comb_dict.values())
        if max_value > 1:
            for comb in comb_dict:
                if comb_dict[comb] == max_value:
                    answer.append("".join(comb))
            comb_dict.clear()

    answer.sort()
    return answer
