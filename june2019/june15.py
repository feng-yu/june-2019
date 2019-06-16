"""
[Medium]

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word.
Pad extra spaces when necessary so that each line has exactly length k.
Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16,
you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

"""
from functools import reduce
from math import ceil

def form_lines(wl, mll):
    ll = list(map(len, wl))
    print(wl)
    print(ll)
    swl = []
    start = 0
    end = 0
    total = 0
    while end < len(wl):
        total += ll[end]
        if total < mll-end+start:
            end += 1
        else:
            if total > mll-end+start:
                end -= 1
            l = wl[start:end+1]
            swl.append(l)
            end += 1
            start = end
            total = 0
    else:
        l = wl[start:]
        swl.append(l)
    print(swl)

    sentences = []
    for sw in swl:
        l = list(map(len, sw))
        total = reduce(lambda x,y: x + y, l)
        print(total)
        total_pad = mll - total
        total_pad_count = len(sw) - 1
        pad = ceil(total_pad / total_pad_count)
        blank = pad * total_pad_count - total_pad
        pad_list = []
        for i in range(total_pad_count - blank):
            pad_list.append(pad)
        for i in range(blank):
            pad_list.append(pad-1)

        print(pad_list)
        sen = sw[0]

        for i in range(1,len(sw)):
            sen += ' '*pad_list[i-1]
            sen += sw[i]
        sentences.append(sen)

    print(sentences)




wl = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
mll = 16
form_lines(wl, mll)



# def form_lines(word_list, max_line_length):
#     lines_list = []
#     if not word_list:
#         return lines_list
#
#     length_list = map(len, word_list)
#     total_length = 0
#     for index, length in enumerate(length_list):
#         total_length += length
#         if total_length == max_line_length - index:
#             s = word_list[0]
#             for i in range(1,index+1):
#                 s += ' '
#                 s += word_list[i]
#             lines_list.append(s)
#             if index < len(word_list)-1:
#                 return lines_list + form_lines(word_list[index+1:], max_line_length)
#             else:
#                 return lines_list
#             break
#         elif total_length > max_line_length - index:
#             word_count = index - 1











    # line_length = length_list[0]
    # i = 1
    # while line_length < max_line_length:
    #     line_length += (1+length_list[i])
    #     i += 1
    # else:
    #     if line_length == max_line_length:
    #         sentence = word_list[0]
    #         for index in range(i):
    #             sentence += ' '
    #             sentence += word_list[index]
    #         lines_list.append(sentence)
    #     else:



