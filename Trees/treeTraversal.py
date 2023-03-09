class treeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right
def inOrdertraverseTree(root):
    if root == None:
        return 
    else:
        inOrdertraverseTree(root.left)
        print(root.val)
        inOrdertraverseTree(root.right)

def postOrdertraverseTree(root):
    if root == None:
        return 
    else:
        inOrdertraverseTree(root.left)
        inOrdertraverseTree(root.right)
        print(root.val)

def preOrdertraverseTree(root):
    if root == None:
        return 
    else:
        print(root.val)
        inOrdertraverseTree(root.left)
        inOrdertraverseTree(root.right)
        

if __name__ == '__main__':
    root = treeNode(5)
    root.left = treeNode(6)
    root.right = treeNode(7)
    preOrdertraverseTree(root)