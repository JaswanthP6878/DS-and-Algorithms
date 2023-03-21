class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BstTree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        def util(root, key):
            if root == None:
                return BSTNode(key)
            if key < root.val:
                root.left = util(root.left, key)
            if key > root.val:
                root.right = util(root.right, key)
            return root
        self.root = util(self.root, key)
    
    def inorder(self):
        def inorder_util(root):
            if root:
                inorder_util(root.left)
                print(root.val)
                inorder_util(root.right)

        inorder_util(self.root)

def inorderSuccesor(node):
    temp = node
    while(temp.left is not None):
        temp = temp.left
    return temp  

def delete_root(root,key):
    if not root: return root
    if key < root.val:
        root.left = delete_root(root.left, key)
    elif key > root.val:
        root.right = delete_root(root.right, key)
    else:
        if root.left is None: 
            '''case where we have root right'''
            ptr = root.right
            root = None
            return ptr
        elif root.right is None:
            '''case where we have root left'''
            ptr = root.left
            root = None
            return ptr
        '''case where we have both left and right i.e 2 children 1 and no child case are taken care
            above
        '''
        ptr = inorderSuccesor(root.right)
        root.val = ptr.val
        root.right = delete_root(root.right, ptr.val)
    return root

def max_val(root):
    temp = root
    while temp.right:
        temp = temp.right
    return temp.val


btree = BstTree()
btree.insert(2)
btree.insert(6)
btree.insert(3)
btree.insert(15)
btree.insert(8)
btree.insert(16)
btree.insert(9)
btree.insert(4)

# btree.inorder()
print()
# btree.root = delete_root(btree.root,6)
# btree.inorder()
print(max_val(btree.root))