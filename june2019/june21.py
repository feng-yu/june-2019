"""
[Medium]

Given a string, find the palindrome that can be made by inserting the fewest number of
characters as possible anywhere in the word. If there is more than one palindrome of
minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).

For example, given the string "race", you should return "ecarace",
since we can add three letters to it (which is the smallest amount to make a palindrome).
There are seven other palindromes that can be made from "race" by adding three letters,
but "ecarace" comes first alphabetically.

As another example, given the string "google", you should return "elgoogle".
"""

def make_palindrome(word):
    result = []
    char_list = list(word)
    index = 0
    if (len(word)) == 1:
        return word
    while len(char_list) > 1:
        r_index = 0
        r_both = False
        if char_list[0] > char_list[-1]:
            if char_list.count(char_list[-1]) <= char_list.count(char_list[0]):
                r_index = -1
        elif char_list[0] == char_list[-1]:
            r_both = True
        else:
            if char_list.count(char_list[0]) > char_list.count(char_list[-1]):
                r_index = -1

        result.insert(index, char_list[r_index])
        result.insert(-(index + 1), char_list[r_index])
        if r_both:
            char_list.pop(-1)
            char_list.pop(0)
        else:
            char_list.pop(r_index)
        index += 1
    if len(char_list) == 1:
        result.insert(index, char_list[0])
    new_word = ''.join(result)
    print(word)
    print(new_word)
    print(f'Inserted {len(new_word) - len(word)} characters')
    return new_word

word = 'race'
print(make_palindrome(word))
print()

word0 = 'I'
print(make_palindrome(word0))
print()

word1 = 'google'
print(make_palindrome(word1))
print()

word2 = 'doctor'
print(make_palindrome(word2))
print()

word3 = 'tomato'
print(make_palindrome(word3))
print()

