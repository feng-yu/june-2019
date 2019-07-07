"""
[Medium]

Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

For example, given the following preorder traversal:

[a, b, d, e, c, f, g]

And the following inorder traversal:

[d, b, e, a, f, c, g]

You should return the following tree:

    a
   / \
  b   c
 / \ / \
d  e f  g

"""

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

class Tree:
    def __init__(self, root):
        self.root = root

    def preorder(self):
        return self.root.preorder()

    def inorder(self):
        return self.root.inorder()

    def postorder(self):
        return self.root.postorder()


def rebuld(preorderl, inorderl):
    r = Node(preorderl[0])
    if len(inorderl) > 1:
        index = inorderl.index(preorderl[0])
        lpre = preorderl[1:index+1]
        rpe = preorderl[index+1:]
        lin = inorderl[:index]
        rin = inorderl[index+1:]
        r.addleft(rebuld(lpre, lin))
        r.addright(rebuld(rpe, rin))
    return r

prelist = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inlist = ['d', 'b', 'e', 'a', 'f', 'c', 'g']

re = rebuld(prelist, inlist)
print(re.postorder())

# root = Node('a')
# b = Node('b')
# c = Node('c')
# d = Node('d')
# e = Node('e')
# f = Node('f')
# g = Node('g')
# b.addleft(d)
# b.addright(e)
# c.addleft(f)
# c.addright(g)
# root.addleft(b)
# root.addright(c)
#
# tree = Tree(root)
#
# print(tree.preorder())
# print(tree.inorder())
# print(tree.postorder())