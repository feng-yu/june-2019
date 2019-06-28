"""
[Medium]

Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs,
and a starting airport, compute the person's itinerary. If no such itinerary exists, return null.
If there are multiple possible itineraries, return the lexicographically smallest one.
All flights must be used in the itinerary.

For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].

Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.

Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A',
you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary.
However, the first one is lexicographically smaller.
"""

data1 = [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')]
data2 = [('SFO', 'COM'), ('COM', 'YYZ')]
data3 = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')]

def itinerary(li, start):
    result = [start]

    while li:
        start_flights = list(filter(lambda x: x[0] == start, li))
        # print('start_flights', start_flights)

        if start_flights:
            if len(start_flights) > 1:
                for flight in start_flights[1:]:
                    if start_flights[0][1] > flight[1]:
                        start_flights[0] = flight
            result.append(start_flights[0][1])

            li.remove(start_flights[0])
            start = start_flights[0][1]

            # print(result)
        else:
            return None

    return result

print(itinerary(data1, 'YUL'))
print(itinerary(data2, 'COM'))
print(itinerary(data3, 'A'))