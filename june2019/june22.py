"""
[Hard]

Given an array of strictly the characters 'R', 'G', and 'B',
segregate the values of the array so that all the Rs come first,
the Gs come second and the Bs come last. You can only swap elements
of the array.

Do this in linear time and in-place.

For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'].
it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

"""

def sort(li):
    first_index = 0
    last_index = -1
    for index in range(len(li)):
        if index + abs(last_index) == len(li):
            break
        if li[index] == 'B':
            while li[last_index] == 'B':
                last_index -= 1
            if li[last_index] == 'R':
                while li[first_index] == 'R':
                    first_index += 1
                li[last_index], li[first_index] = li[first_index], li[last_index]
                li[index], li[last_index] = li[last_index], li[index]
            else:
                li[index], li[last_index] = li[last_index], li[index]
        elif li[index] == 'R':
            if index != first_index:
                while li[first_index] == 'R':
                    first_index += 1
                li[index], li[first_index] = li[first_index], li[index]

    return li

data = ['G', 'B', 'R', 'R', 'B', 'R', 'G']
#data = ['R', 'B', 'R', 'R', 'B', 'R', 'G']
# data = ['R', 'B', 'G']
# data = ['R',  'G']
print(data)
print()
print(sort(data))