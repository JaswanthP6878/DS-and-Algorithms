from TreeDS import Node
def view(root): 
    '''printing the top side view'''
    mp = dict()
    q = [(root,0)]
    while q:
        ptr = q.pop(0)
        if ptr[1] not in mp:
            mp[ptr[1]] = ptr[0]
        if ptr[0].left:
            q.append((ptr[0].left, ptr[1]-1))
        if ptr[0].right:
            q.append((ptr[0].right, ptr[1]+1))
    
    for k in sorted(mp):
        print(mp[k].val, end = " ")

tree1 = Node(4)
tree1.left = Node(5)
tree1.left.left = Node(9)
tree1.right = Node(5) 

view(tree1)
