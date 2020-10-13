class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None

def minimumDepthBinaryTree(root):
    if root is None:
        return 0
    elif root.right is None:
        return minimumDepthBinaryTree(root.left) + 1
    elif root.left is None:
        return minimumDepthBinaryTree(root.right) + 1
    else:
        return min(minimumDepthBinaryTree(root.left), minimumDepthBinaryTree(root.right)) + 1


tree = Tree(5)
tree.left = Tree(12)
right = Tree(32)
right.right = Tree(4)
right.left = Tree(8)
tree.right = right

print(minimumDepthBinaryTree(tree))