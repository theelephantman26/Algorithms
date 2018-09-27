## DO NOT EDIT THIS CLASS
class Node:
    # A binary search tree node class in Python3
    def __init__(self, n):
        self.key = n  # Set the key to number n
        self.left = None  # Currently left child is a leaf denoted by None
        self.right = None  # right child is a leaf denoted by None

    def addLeftSubtree(self, lNode):  # Replace the left child with lNode
        self.left = lNode

    def addRightSubtree(self, rNode):  # Replace the right child with rNode
        self.right = rNode

    def addSubtree(self, lNode, rNode):  # Add both left and right nodes
        self.addLeftSubtree(lNode)
        self.addRightSubtree(rNode)

def checkNodePosition(key, parent_nodes, sub_tree):
    parent_nodes.append([key, sub_tree])
    result = True
    for i in range(0, len(parent_nodes)-1):
        if parent_nodes[i+1][1] is -1:
            result = result and parent_nodes[i][0] > key
        else:
            result = result and parent_nodes[i][0] < key
    del parent_nodes[-1]
    return result

def isBinarySearchTree(rootNode, parent_nodes=list(), sub_tree=0):
    if rootNode is not None:
        parent_nodes.append([rootNode.key, sub_tree])
    if rootNode is None:
        return True
    elif (rootNode.left is None or checkNodePosition(rootNode.left.key, parent_nodes, -1)) and (rootNode.right is None or checkNodePosition(rootNode.right.key, parent_nodes, +1)):
        result = True and isBinarySearchTree(rootNode.left, parent_nodes, -1) and isBinarySearchTree(rootNode.right, parent_nodes, 1)
        del parent_nodes[-1]
        return result
    else:
        return False

## END-DO NOT EDIT## THIS IS TEST CODE.
## TEST CODE: DO NOT EDIT

# Tree number 1

node4 = Node(1)
node5 = Node(-1)
node6 = Node(3)

node4.addSubtree(node5, node6)

node1 = Node(20)
node1.addLeftSubtree(node4)

node2 = Node(30)
node3 = Node(40)
node2.addLeftSubtree(node1)
node2.addRightSubtree(node3)

rootNode1 = node2


# Tree number 2

node1 = Node(15)
node2 = Node(54)
node3 = Node(45)
node3.addSubtree(node2, node1)
node4 = Node(115)
node5 = Node(94)
node5.addSubtree(node3, node4)
node6 = Node(18)
node7 = Node(23)
node9 = Node(20)
node9.addSubtree(node6, node7)

rootNode2 = Node(55)
rootNode2.addSubtree(node9, node5)

# Tree number 3

rootNode3 = Node(20)

# Tree number 4

node11 = Node(18)
node12 = Node(26)
node13 = Node(12)
node14 = Node(29)

node11.addSubtree(None, node12)
node12.addSubtree(node13, node14)

rootNode4 = node11

try:
    assert isBinarySearchTree(rootNode1), 'Test 1 Failed: expected answer True, your answer False'
    print('Test 1 Passed!')
    assert not isBinarySearchTree(rootNode2), 'Test 2 Failed: expected answer False, your answer True'
    print('Test 2 Passed!')
    assert isBinarySearchTree(rootNode3), 'Test 3 Failed: expected answer True, your answer False'
    print('Test 3 Passed!')
    assert not isBinarySearchTree(rootNode4), 'Test 3 Failed: expected answer False, your answer True'
    print('Test 4 Passed!')

except NotImplementedError:
    display(HTML('<font color="red"> Nothing Implemented Yet. </font>'))

## END-DO NOT EDIT

