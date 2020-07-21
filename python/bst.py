class Node:
    def __init__(self,val):
        self.l_child = None
        self.r_child = None
        self.val = val

class BinarySearchTree(object):
    def insert(self, root, node):
        
        # if there is no root, set node as root
        
        if root is None:
            return node
        
        # if node value > root value
        #   insert node as right child
        #
        # if node value < root value
        #   insert node as left child

        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)

        return root
    
    # In Order Traversal
    #   1. Check if there is left child. If yes, check until there is none.
    #   2. Take the root value
    #   3. Check if there is right child. If yes, check until there is none.

    def in_order_place(self, root):
        if not root:
            return None
        else:
            self.in_order_place(root.l_child)
            print(root.val)
            self.in_order_place(root.r_child)

    # Pre Order Traversal
    #   1. Take the root value
    #   2. Check if there is left child. If yes, check until there is none.
    #   3. Check if there is right child. If yes, check until there is none.

    def pre_order_place(self, root):
        if not root:
            return None
        else:
            print(root.val)
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    # Post Order Traversal
    #   1. Check if there is left child. If yes, check until there is none.
    #   2. Check if there is right child. If yes, check until there is none.
    #   3. Take the root value

    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print(root.val)
    
    # Check if a tree is a binary search tree
    #
    # isBST(root, l_child, r_child)
    #   root = the root or the parent node
    #   l_child = the left child of the root
    #   r_child = the right child of the root
def isBST(root, l_child = None, r_child = None):
    # if root is None, therefore it is empty. Returns True
    # empty node is a Binary Search Tree
    if root is None:
        return True
    
    # Check if there is left child. If yes, check the if left child's value is
    # greater than the root's value. If yes, return False. It is not a 
    # Binary Search Tree
    if l_child != None and root.val <= l_child.val:
        return False
    
    # Check if there is right child. If yes, check if the right child's value is
    # greater than the root's value. If yes, return False. It is not a 
    # Binary Search Tree
    if r_child != None and root.val>= r_child.val:
        return False

    # Check the remaining left and right sub trees recursively. Return True
    # if sub trees are also Binary Search Trees
    return isBST(root.l_child, l_child, root) and isBST(root.r_child, root, r_child)

# Print node by level using queues
def printLevelOrder(root):

    # if root is None, return. There is nothing down here
    if root is None:
        return

    # create a queue
    queue = []

    # the queue starts with root
    queue.append(root)

    # print the node values in queue. First come first serve.
    while len(queue) > 0:

        # print the node value in front of queue. Then move on to the next customer.
        print(queue[0].val)
        node = queue.pop(0)

        # if the last customer have left child, the child becomes the next customer
        if node.l_child is not None:
            queue.append(node.l_child)

        # if the last customer have right child, the child become the next customer
        if node.r_child is not None:
            queue.append(node.r_child)
