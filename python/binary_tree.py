

from trees import *


A = BinaryTreeNode("A")
B = BinaryTreeNode("B")
C = BinaryTreeNode("C")
D = BinaryTreeNode("D")
E = BinaryTreeNode("E")
F = BinaryTreeNode("F")
G = BinaryTreeNode("G")
H = BinaryTreeNode("H")
I = BinaryTreeNode("I")
J = BinaryTreeNode("J")

E.l_child = H
G.l_child = I
G.r_child = J
B.l_child = D
B.r_child = E
C.l_child = F
C.r_child = G
A.l_child = B
A.r_child = C

root = A
postorderTraversal(root)

