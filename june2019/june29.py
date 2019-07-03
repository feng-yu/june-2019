"""
[Hard]

Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k.
If such a subset cannot be made, then return null.

Integers can appear more than once in the list. You may assume all numbers in the list are positive.

For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
"""


def find_set(li, k):
    if li:
        li.sort()
        result = []
        if k in li:
            result.append(k)
            return result
        if k < li[0]:
            result.clear()
        else:
            for i in li:
                sub_li = li.copy()
                sub_li.remove(i)
                sub_result = find_set(sub_li, k-i)
                if sub_result:
                    result.append(i)
                    for sub_i in sub_result:
                        result.append(sub_i)
                    return result
                else:
                    result.clear()


data = [12, 1, 61, 5, 9, 2]
data1 = [1, 2, 12]
k = 27

re = find_set(data, k)
print(re)