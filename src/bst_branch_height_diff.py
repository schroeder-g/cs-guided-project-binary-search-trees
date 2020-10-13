# Determine if the tree is balanced by ensuring that the maximum diff
# in each branch height is <= 1.
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None


# function to find height of binary tree
def height(root):
    # base condition when binary tree is empty
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


# function to check if tree is height-balanced or not
def balancedBinaryTree(root):
    # Base condition
    if root is None:
        return True

    # for left and right subtree height
    lh = height(root.left)
    rh = height(root.right)

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1) and balancedBinaryTree(
            root.left) is True and balancedBinaryTree(root.right) is True:
        return True

    # if we reach here means tree is not
    # height-balanced tree
    return False


tree = Tree(5)
tree.left = Tree(12)
right = Tree(32)
right.right = Tree(4)
right.left = Tree(8)
tree.right = right

print(balancedBinaryTree(tree))
