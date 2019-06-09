"""
[Easy]
Given two singly linked lists that intersect at some point,
find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
"""


class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def add_next(self, node):
        self.next = node

    def get_next(self):
        return self.next

    def has_next(self):
        return self.next != None

    def __str__(self):
        return f' -> %s' % (self.value)

    def __eq__(self, other_node):
        return self.value == other_node.value


class LinkedList():
    def __init__(self, root):
        self.root = root

    def get_root(self):
        return self.root

    def print_list(self):
        current_node = self.root
        while current_node:
            print(current_node, end='')
            current_node = current_node.get_next()
        print('')

    def add_node(self, value):
        node = Node(value)
        node.add_next(self.root)
        self.root = node

    def has_node(self, node):
        current_node = self.root
        while current_node and current_node != node:
            current_node = current_node.get_next()
        if current_node:
            return True
        else:
            return False


def find_intersect(linked_list1, linked_list2):
    current_node = linked_list1.get_root()
    while current_node and (not linked_list2.has_node(current_node)):
        current_node = current_node.get_next()
    if current_node:
        return current_node
    else:
        return None

node1 = Node(10)

linked_list1 = LinkedList(node1)
linked_list1.add_node(8)
linked_list1.add_node(7)
linked_list1.add_node(3)
linked_list1.print_list()

linked_list2 = LinkedList(node1)
linked_list2.add_node(8)
linked_list2.add_node(1)
linked_list2.add_node(99)
linked_list2.print_list()
print(linked_list2.has_node(Node(1)))

intersecting_node = find_intersect(linked_list1, linked_list2)
print(intersecting_node)
