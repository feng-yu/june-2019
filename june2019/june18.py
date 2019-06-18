"""
[Easy]

The edit distance between two strings refers to the minimum number of character insertions,
deletions, and substitutions required to change one string to the other.
For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""
import itertools
import functools


def edit_diff(s1, s2):
    """
    Using the zip_longest function from itertools
    :param s1:
    :param s2:
    :return: the edit difference between two strings
    """
    li = itertools.zip_longest(s1, s2)
    total = 0
    for item in li:
        if item[0] != item[1]:
            total += 1
    return total


def edit_diff1(s1, s2):
    """
    Uisng itertools.zip_longest and map function
    :param s1:
    :param s3:
    :return: edit difference between two strings
    """
    li = list(itertools.zip_longest(s1, s2))
    di_list = map(lambda x: 1 if x[0] != x[1] else 0, li)
    return sum(di_list)


def edit_diff2(s1, s2):
    """
    Using itertools.zip_longest and functools.reduce functions
    :param s1:
    :param s2:
    :return: edit difference between two strings
    """
    li = list(itertools.zip_longest(s1, s2))
    total = functools.reduce(lambda a, b: a + b, map(lambda x: 1 if x[0] != x[1] else 0, li))
    return total


def edit_diff3(s1, s2):
    """
    Most dump solution
    :param s1:
    :param s2:
    :return: edit difference between two strings
    """
    l_s1 = len(s1)
    l_s2 = len(s2)
    if l_s1 >= l_s2:
        total = l_s1 - l_s2
        short = s2
        long = s1
    else:
        total = l_s2 - l_s1
        short = s1
        long = s2

    for i, c in enumerate(short):
        if c != long[i]:
            total += 1

    return total


s1 = 'kitten'
s2 = 'sitting'
print('difference', edit_diff3(s2, s1))

