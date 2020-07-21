import bst

r  = bst.Node(3)
node = bst.BinarySearchTree()
nodeList = [1, 8, 5, 12, 14, 6, 15, 7, 16, 8]

for nd in nodeList:
     node.insert(r, bst.Node(nd))
print("------In order ---------")
print (node.in_order_place(r))
print("------Pre order ---------")
print (node.pre_order_place(r))
print("------Post order ---------")
print (node.post_order_place(r))
print(bst.is_BST(r))
