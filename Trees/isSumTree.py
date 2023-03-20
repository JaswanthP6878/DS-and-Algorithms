from TreeDS import Node

def sumofTree(root):
    if not root:
        return 0
    else :
        return root.val + sumofTree(root.left) + sumofTree(root.right)

def isSumTree(root):
    if not root:
        return True
    elif not root.left and not root.right:
        return True
    else:
        return root.val == sumofTree(root.left) + sumofTree(root.right) and isSumTree(root.left) and isSumTree(root.right)

tree1 = Node(2)
tree1.left = Node(2) 
tree1.left.left = Node(1)
tree1.left.right = Node(1)

print(isSumTree(tree1))

