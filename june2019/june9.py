"""
[medium]

Given a dictionary of words and a string made up of those words (no spaces),
return the original sentence in a list. If there is more than one possible reconstruction,
return any of them. If there is no possible reconstruction, then return null.

For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].

Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond',
and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].
"""


def find_sentence(dic, string):
    result = []
    for word in dic:
        if string.startswith(word):
            result.append(word)
            string = string[len(word):]
            break
    else:
        return None
    if len(string) != 0:
        result  += find_sentence(dic, string)
    return result


dic1 = ('quick', 'brown', 'the', 'fox')
dic2 = ('bed', 'bath', 'bedbath', 'and', 'beyond')
string1 = 'thequickbrownfox'
string2 = 'bedbathandbeyond'

result1 = find_sentence(dic1, string1)
print(result1)

result2=find_sentence(dic2, string2)
print(result2)
