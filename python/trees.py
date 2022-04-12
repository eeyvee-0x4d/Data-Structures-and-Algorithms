# Book: Necaise R.D Data structures and algorithms using Python
# 		Chapter 13.2 Binary Trees p.373

class BinaryTreeNode:
	def __init__(self, val):
		self.value = val
		self.l_child = None
		self.r_child = None

"""
Pre order traversal of a binary tree is done by
starting from the root node traverses the left
subtree of the node. If no left subtree is found,
the right subtree is traversed.
"""
def preorderTraversal(subtree):
	if subtree is not None:
		print(subtree.value)
		preorderTraversal(subtree.l_child)
		preorderTraversal(subtree.r_child)

"""
In order traversal traveses a binary tree in a left-right
and top-down manner. The traversal starts from the
left most node of the binary tree and work its way
up to the right most node.
"""
def inorderTraversal(subtree):
	if subtree is not None:
		inorderTraversal(subtree.l_child)
		print(subtree.value)
		inorderTraversal(subtree.r_child)

"""
Post order traversal traverses a binary tree in a
left-right and down-top manner. The traversal is same
as the indorder traversal except the deepest node is
traversed first
"""
def postorderTraversal(subtree):
	if subtree is not None:
		postorderTraversal(subtree.l_child)
		postorderTraversal(subtree.r_child)
		print(subtree.value)