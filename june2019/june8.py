"""
[Easy]
Given an array of time intervals (start, end) for classroom lectures (
possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
"""


def find_min_rooms(ta):
    ta = sorted(ta, key=lambda x:x[0])
    rooms = []
    for time_interval in ta:
        if len(rooms) == 0:
            new_room = [time_interval]
            rooms.append(new_room)
        else:
            need_new_room = True
            for room in rooms:
                if time_interval[0] > room[-1][1]:
                    room.append(time_interval)
                    need_new_room = False
                    break
                else:
                    for time_indics in range(len(room)-1):
                        if time_interval[0] > room[time_indics][1] and time_interval[1] < room[time_indics+1][0]:
                            room.insert(time_interval, time_indics+1)
                            need_new_room = False
                            break
                if not need_new_room:
                    break
            if need_new_room:
                rooms.append([time_interval])

    print(rooms)
    return len(rooms)


ta = [(30, 75), (0, 50), (60, 150), (52, 58), (80, 90), (10, 20)]
rooms_count = find_min_rooms(ta)
print(rooms_count)

