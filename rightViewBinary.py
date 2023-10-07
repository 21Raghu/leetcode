

class Node:
    # A constructor to create a new Binary tree Node
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


from collections import defaultdict

def rightViewUtil(root, level):
    if root is None:
        return

    if level not in l:
        l[level] = root.data

    rightViewUtil(root.right,level + 1)
    rightViewUtil(root.left, level + 1)
    return l.values()

l = defaultdict()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(rightViewUtil(root,0))

