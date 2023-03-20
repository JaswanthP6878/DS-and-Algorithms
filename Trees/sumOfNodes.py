from TreeDS import Node;
tree1 = Node(4)
tree1.left = Node(5) 
tree1.right = Node(5) 

tree2 = Node(4)
tree2.left = Node(5) 
tree2.right = Node(6) 

def SumOfNodes(root):
    if not root:
        return 0
    else:
        return root.val + SumOfNodes(root.left) + SumOfNodes(root.right)

print(SumOfNodes(tree2))

