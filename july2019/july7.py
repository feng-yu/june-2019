"""
[Medium}

Suppose an arithmetic expression is given as a binary tree.
Each leaf is an integer and each internal node is one of '+', '−', '∗', or '/'.

Given the root to such a tree, write a function to evaluate it.

For example, given the following tree:

    *
   / \
  +    +
 / \  / \
3  2  4  5

You should return 45, as it is (3 + 2) * (4 + 5).
"""
import operator

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def addleft(self, left):
        self.left = left

    def addright(self, right):
        self.right = right

    def preorder(self):
        result = []
        result.append(self.value)
        if self.left:
            result = result + self.left.preorder()
        if self.right:
            result += self.right.preorder()
        return result

    def inorder(self):
        result = []
        if self.left:
            result += self.left.inorder()
        result.append(self.value)
        if self.right:
            result += self.right.inorder()
        return result

    def postorder(self):
        result = []
        if self.left:
            result += self.left.postorder()
        if self.right:
            result += self.right.postorder()
        result.append(self.value)
        return result

    def evaluate(self):
        operationlist = ['+', '-', '*', '/']
        if self.value not in operationlist:
            return self.value
        else:
            if self.value == '+':
                op = operator.add
            elif self.value == '-':
                op = operator.sub
            elif self.value == '*':
                op = operator.mul
            else:
                op = operator.truediv
            return op(self.left.evaluate(), self.right.evaluate())

class Tree:
    def __init__(self, root):
        self.root = root

    def preorder(self):
        return self.root.preorder()

    def inorder(self):
        return self.root.inorder()

    def postorder(self):
        return self.root.postorder()

    def evaluate(self):
        return self.root.evaluate()


root = Node('*')
fleft = Node('+')
fright = Node('+')
slleft = Node(3)
slright = Node(2)
srleft = Node(4)
srright = Node(5)
fleft.addleft(slleft)
fleft.addright(slright)
fright.addleft(srleft)
fright.addright(srright)
root.addleft(fleft)
root.addright(fright)

tree = Tree(root)
print(tree.evaluate())

