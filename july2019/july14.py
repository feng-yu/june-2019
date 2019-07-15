"""
[Medium]

Given a string s and an integer k, break up the string into multiple lines such that each line has a length of k or less.
You must break it up so that words don't break across lines. Each line has to have the maximum possible amount of words.
If there's no way to break the text up, then return null.

You can assume that there are no spaces at the ends of the string and that there is exactly one space between each word.

For example, given the string "the quick brown fox jumps over the lazy dog" and k = 10,
you should return: ["the quick", "brown fox", "jumps over", "the lazy", "dog"].
No string in the list has a length of more than 10.
"""
def breakstr(string, k):
    result = []
    words = string.strip().split()
    print(words)

    current_index = 0
    words_count = len(words)
    while current_index < words_count:
        word_length = len(words[current_index])
        if word_length > k:
            return None
        else:
            line = words[current_index]
            if current_index + 1 < words_count:
                next_word_length = len(words[current_index + 1])
                while next_word_length + word_length + 1 <= k:
                    line += ' '
                    line += words[current_index + 1]
                    word_length += (next_word_length + 1)
                    current_index += 1
                    if current_index + 1 < words_count:
                        next_word_length = len(words[current_index + 1])
                    else:
                        break
            result.append(line)
            current_index += 1

    return result

data = 'the quick brown fox jumps over the lazy dog'
print(breakstr(data, 10))

