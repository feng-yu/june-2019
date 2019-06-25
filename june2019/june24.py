"""
[Easy]

The power set of a set is the set of all its subsets.
Write a funciton that, given a set, generates its power set.

For example, givn the set {1, 2, 3} it should return:
{{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
"""

def power_set(s):
    li = list(s)
    result = [[]]
    if not li:
        return result
    for index, element in enumerate(li):
        si_li = [element]
        result.append(si_li)
        inter_result = power_set(li[index+1:])
        for inter_ele in inter_result:
            n_list = si_li + inter_ele
            if n_list not in result:
                result.append(n_list)
    return result


def power_set1(s):
    li = list(s)
    result = [[]]
    if not li:
        return result
    for index, element in enumerate(li):
        si_li = [element]
        result.append(si_li)
        inter_result = power_set(li[index+1:])
        for inter_ele in inter_result:
            n_list = si_li + inter_ele
            if n_list not in result:
                result.append(n_list)

    s_result = set()
    for e in result:
        s_result.add(frozenset(e))
    return s_result


data = [1, 2, 3]
print(power_set1(data))




