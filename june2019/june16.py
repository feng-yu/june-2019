"""
[Easy]

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding.
You can assume the string to be encoded have no digits and consists solely of alphabetic characters.
You can assume the string to be decoded is valid.
"""


def encoding(s):
    result = ''
    while s:
        character = s[0]
        count = 1
        while count < len(s) and character == s[count]:
            count += 1
        else:
            result += str(count)
            result += character
            s = s[count:]
    return result


def decoding(s):
    result = ''
    while s:
        count = s[0]
        character = s[1]
        result += character * int(count)
        s = s[2:]
    return result


origin = 'AAAABBBCCDAA'
result = encoding(origin)
print(result)
if result == '4A3B2C1D2A':
    print('You got it!')
else:
    print('Take another look!')


origin = '4A3B2C1D2A'
result = decoding(origin)
print(result)
if result == 'AAAABBBCCDAA':
    print('Decoded successfully!')
else:
    print('Decoded wrongly, please take another look')

