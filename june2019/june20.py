"""
[Easy]

Compute the running median of a sequence of numbers.
That is, given a stream of numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle numbers.

For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:

2
1.5
2
3.5
2
2
2

"""

def running_median(li):
    for index, _ in enumerate(li):
        if index == 0:
            print(li[index])
        else:
            temp_li = li[:index+1]
            temp_li.sort()
            temp_li_len = len(temp_li)
            i = temp_li_len // 2
            if temp_li_len % 2 == 0:
                print((temp_li[i] + temp_li[i-1]) / 2)
            else:
                print(temp_li[i])

data = [2, 1, 5, 7, 2, 0, 5]
running_median(data)

