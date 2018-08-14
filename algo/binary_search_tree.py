from algo.util import partition


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


def inorder_recursive(root):
    """
    Inorder recursive traversal of a binary search tree using generators

    :type root: TreeNode
    :rtype val: any
    """
    if root:
        yield from inorder_recursive(root.left)
        yield root.val
        yield from inorder_recursive(root.right)


def inorder_stack(root):
    """
    Inorder not recoursive traversal of a binary search tree using generators

    :type root: TreeNode
    :rtype val: any
    """
    stack = []
    current = root
    while True:
        while current is not None:
            stack.append(current)
            current = current.left

        if not stack:
            break

        current = stack.pop()
        yield current.val
        current = current.right


def isValidBST(root):
    """
    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

        1. The left subtree of a node contains only nodes with keys
            less than the node's key.
        2. The right subtree of a node contains only nodes with keys
            greater than the node's key.
        3. Both the left and right subtrees must also be binary search trees.

    :type root: TreeNode
    :rtype: bool
    """
    for item1, item2 in partition(list(inorder_stack(root)), 2, 1):
        if item1 >= item2:
            return False

    return True


def valid_bst(node, min_val, max_val):
    """
    Given a binary tree, determine if it is a valid binary search tree (BST).

    Assume a BST is defined as follows:

        1. The left subtree of a node contains only nodes with keys
            less than the node's key.
        2. The right subtree of a node contains only nodes with keys
            greater than the node's key.
        3. Both the left and right subtrees must also be binary search trees.

    :type root: TreeNode
    :rtype: bool
    """
    if not node:
        return True
    if node.val <= min_val or node.val >= max_val:
        return False
    return valid_bst(node.left, min_val, node.val) and valid_bst(
        node.right, node.val, max_val
    )


def searchBST(root, val):
    """
    Given the root node of a binary search tree (BST) and a value.
    You need to find the node in the BST that the node's value equals
    the given value. Return the subtree rooted with that node.
    If such node doesn't exist, you should return NULL.

    :type root: TreeNode
    :type val: int
    :rtype: TreeNode
    """
    if root is None:
        return
    elif root.val < val:
        return searchBST(root.right, val)
    elif root.val > val:
        return searchBST(root.left, val)
    else:
        return root


def lowestCommonAncestor(root, p, q):
    """
    Given a binary search tree (BST), find the lowest common
    ancestor (LCA) of two given nodes in the BST.

    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None

    if root.val > p and root.val > q:
        return lowestCommonAncestor(root.left, p, q)
    elif root.val < p and root.val < q:
        return lowestCommonAncestor(root.right, p, q)
    else:
        return root


def lowestCommonAncestor_II(root, p, q):
    """
    Given a binary search tree (BST), find the lowest common
    ancestor (LCA) of two given nodes in the BST.

    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None

    if root.val == p or root.val == q:
        return root

    left_found = lowestCommonAncestor_II(root.left, p, q)
    right_found = lowestCommonAncestor_II(root.right, p, q)

    if left_found and right_found:
        return root  # lca
    elif left_found:
        return left_found
    elif right_found:
        return right_found
