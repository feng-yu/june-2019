"""
[Medium]

Given a singly linked list and an integer k, remove the kth last element from the list.
k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.root = None
        self.length = 0

    def add_node(self, value):
        node = Node(value)
        node.next = self.root
        self.root = node
        self.length += 1

    def get_length(self):
        return self.length

    def print_list(self):
        current_node = self.root
        while current_node:
            print(f' -> %i' % current_node.value, end='' )
            current_node = current_node.next

    def delete_kth_last_node(self, k):
        """The last kth node is total-k node from the root. The root is zero"""
        current_node = self.root
        for _ in range(1, self.length-k):  #find node before the last kth node
            current_node = current_node.next
        current_node.next = current_node.next.next
        self.length -= 1


ll = LinkedList()
for i in range(10):
    ll.add_node(i)
print(f'The length of linked list: %i' % ll.get_length())
ll.print_list()
print()
ll.delete_kth_last_node(2)
print('After delete the 2nd to last node')
print(f'The length of linked list: %i' % ll.get_length())
ll.print_list()
print()
