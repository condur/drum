from algo import binary_search_tree as bst


def test_tree_traversal():
    node1 = bst.TreeNode(1)
    node3 = bst.TreeNode(3)
    node2 = bst.TreeNode(2, node1, node3)
    node5 = bst.TreeNode(5)
    node4 = bst.TreeNode(4, node2, node5)
    assert list(bst.inorder_recursive(node4)) == [1, 2, 3, 4, 5]
    assert list(bst.inorder_stack(node4)) == [1, 2, 3, 4, 5]


def test_isValidBST():
    node1 = bst.TreeNode(1)
    node3 = bst.TreeNode(3)
    node2 = bst.TreeNode(2, node1, node3)
    node5 = bst.TreeNode(5)
    node4 = bst.TreeNode(4, node2, node5)
    assert bst.isValidBST(node4) is True


def test_searchBST():
    node1 = bst.TreeNode(1)
    node3 = bst.TreeNode(3)
    node2 = bst.TreeNode(2, node1, node3)
    node5 = bst.TreeNode(5)
    node4 = bst.TreeNode(4, node2, node5)
    assert bst.searchBST(node4, 3) == node3
