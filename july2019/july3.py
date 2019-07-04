"""
[Hard]

Given a string, find the longest palindromic contiguous substring.
If there are more than one with the maximum length, return any one.

For example, the longest palindromic substring of "aabcdcb" is "bcdcb".
The longest palindromic substring of "bananas" is "anana".
"""

def find_longest_palindromic(string):
    two_char_set = set()
    palindromic_list = []

    for c in string:
        if string.count(c) > 1:
            two_char_set.add(c)

    if two_char_set:
        for c in two_char_set:
            begin_index = string.index(c)
            end_index = string.rindex(c)
            sub_string = string[begin_index:end_index+1]
            sub_string_list = list(sub_string)
            sub_string_list_copy = sub_string_list
            sub_string_list.reverse()
            if sub_string_list == sub_string_list_copy:
                palindromic_list.append(sub_string)

    if palindromic_list:
        max_length = 0
        max_length_index = 0
        for i, p in enumerate(palindromic_list):
            if len(p) > max_length:
                max_length = len(p)
                max_length_index = i
        return palindromic_list[max_length_index]

data = 'aabcdcb'
print('data', data)
print(find_longest_palindromic(data))

print()

data1 = 'bananas'
print('data1', data1)
print(find_longest_palindromic(data1))

