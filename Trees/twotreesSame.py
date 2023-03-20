class Node:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def compare(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 and root2:
        return root1.val == root2.val and compare(root1.left, root2.right) and compare(root1.right, root2.right)
    else :
        return False

tree1 = Node(4)
tree1.left = Node(5) 
tree1.right = Node(5) 

tree2 = Node(4)
tree2.left = Node(5) 
tree2.right = Node(6) 

print(compare(tree1, tree2))




