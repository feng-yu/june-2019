"""
[easy]

You run an e-commerce website and want to record the last N order ids in a log.
Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
"""
class OrderLog:
    def __init__(self, N):
        self.circular_log = [None] * N
        self.current_index = 0

    def record(self, order_id):
        self.circular_log[self.current_index] = order_id
        self.current_index += 1
        if self.current_index == len(self.circular_log):
            self.current_index = 0

    def get_last(self, i):
        return self.circular_log[self.current_index -i]

    def __str__(self):
        string = ''
        for i in self.circular_log:
            string += f'{i} '
        return string

ol = OrderLog(5)
ol.record(0)
ol.record(1)
ol.record(2)
ol.record(3)
ol.record(4)
ol.record(5)
print(ol)
print(ol.get_last(3))
