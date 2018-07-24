# Tree

A tree is a data structure similar to a linked List but instead of each node pointing simply to the next node in a linear fashion, each node points to a number of nodes. Tree is an example of non-linear data structures. A tree structure is a way of representing the hierarchical nature of a structure in a graphical form.

In trees ADT (Abstract Data Type), the order of the elements is not important. If we need ordering information linear data structures like linked lists, stacks, queues, elc. can be used.

## Glossary

• The _root_ of a tree is the node with no parents. There can be at most one root node in a tree.
• An _edge_ refers to the link from parent to child.
• A node with no children is called _leaf node_.
• Children of same parent arc called _siblings_.
• A node p is an _ancestor_ of node q if there exists a path from root to q and appears on the path. The node q is called a _descendant_ of p.
• The set of all nodes at a given depth is called the _level_ of the tree. The root node is at level zero.
• The _depth_ of a node is the length of the path from the root to the node.
• The _height_ of a node is the length of the path from that node to the deepest node. The height of a tree is the length of the path from the root to the deepest node in the tree. A (rooted) tree with only one node (the root) has a height of zero.
• _Height of the tree_ is the maximum height among all the nodes in the tree and _depth of the tree_ is the maximum depth among all the nodes in the tree.
• The size of a node is the number of descendants it has including itselfs.
• If every node in a tree has only one child (except leaf nodes) then we call such trees _skew trees_. If every node has only left child then we call them left skew trees. Similarly, if every node has only right child then we call them right skew trees.

## Tree Traversals

In order to process trees, we need a mechanism for traversing them. The process of visiting all nodes of a tree is called tree traversal. Each node is processed only once but it may be visited more than once. 

Tree traversal is like searching the tree, except that in traversal the goal is to move through the tree in a particular order. In addition, all nodes are processed in the traversal by searchinq stops when the required node is found.

### Traversal Possibilities

Starting at the root of a binary tree, there are three main steps that can be performed and the order in which they are performed defines the traversal type. These steps are: performing an action on the current node (referred to as "visiting" the node und denoted with "D"), traversing to the left child node (denoted with "L"), and traversing to the right child node (denoted with "R"). This process can be easily described through recursion. Based on the above definition there arc 6 possibilities:

I. LDR: Process left subtree, process the current node data and then process right subtree
2. LRD: Process left subtree, process right subtree and then process the current node data
3. DLR: Process the current node data, process left subtree and then process right subtree
4. DRL: Process the current node data, process right subtree and then process left subtree
5. RDL: Process right subtree, process the current node data and then process left subtree
6. RLD: Process right subtree, process left subtree and then process the current node data

### Classifying the Traversals

The sequence in which these entities (nodes) are processed defines a particular traversal method. The classification is based on the order in which current node is processed. That means, if we are classifying based on current node (D) and if D comes in the middle then it does not matter whether L is on left side of D or R is on left side of D. Similarly, it does not matter whether L is on right side of D or R is on right side of D. Due to this, the total 6 possibilities are reduced to 3 and these are:

• Preorder (DLR) Traversal
• Inorder (LDR) Traversal
• Postorder (LRD) Traversal

There is another traversal method which does not depend on the nbovc orders and it is:
• Level Order Traversal: This method is inspired from Breadth First Search (BFS of Graph algorithms).


