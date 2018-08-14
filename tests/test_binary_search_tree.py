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


def test_lowestCommonAncestor():
    node3 = bst.TreeNode(3)
    node5 = bst.TreeNode(5)
    node4 = bst.TreeNode(4, node3, node5)
    node0 = bst.TreeNode(0)
    node2 = bst.TreeNode(2, node0, node4)
    node7 = bst.TreeNode(7)
    node9 = bst.TreeNode(9)
    node8 = bst.TreeNode(8, node7, node9)
    node6 = bst.TreeNode(6, node2, node8)
    assert bst.lowestCommonAncestor(node6, 3, 5) == node4
    assert bst.lowestCommonAncestor(node6, 2, 8) == node6

    assert bst.lowestCommonAncestor_II(node6, 3, 5) == node4
    assert bst.lowestCommonAncestor_II(node6, 2, 8) == node6
