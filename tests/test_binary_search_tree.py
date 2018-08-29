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


def test_maxDepth():
    node1 = bst.TreeNode(1)
    node3 = bst.TreeNode(3)
    node2 = bst.TreeNode(2, node1, node3)
    node5 = bst.TreeNode(5)
    node4 = bst.TreeNode(4, node2, node5)
    assert bst.maxDepth(node4) == 3
    assert bst.maxDepth_II(node4) == 3
    assert bst.maxDepth_III(node4) == 3


def test_isSymmetric():
    node3_l = bst.TreeNode(3)
    node3_r = bst.TreeNode(3)
    node4_l = bst.TreeNode(4)
    node4_r = bst.TreeNode(4)
    node2_left = bst.TreeNode(2, node3_l, node4_l)
    node2_right = bst.TreeNode(2, node4_r, node3_r)
    node1 = bst.TreeNode(1, node2_left, node2_right)
    assert bst.isSymmetric(node1) is True


def test_sortedArrayToBST():
    assert (
        len(list(bst.inorder_recursive(bst.sortedArrayToBST([-10, -3, 0, 5, 9])))) == 5
    )
    assert (
        len(list(bst.inorder_recursive(bst.sortedArrayToBST_II([-10, -3, 0, 5, 9]))))
        == 5
    )
