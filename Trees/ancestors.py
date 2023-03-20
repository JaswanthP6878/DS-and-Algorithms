from TreeDS import Node
#iterative approach example
def ancestors(root, val):
    parents = {root.val: None}
    que = [root]
    while len(que) > 0:
        p = que.pop(0)
        if p.val == val: break
        if p.left:
            que.append(p.left)
            parents[p.left.val] = p.val
        if p.right:
            que.append(p.right)
            parents[p.right.val] = p.val
    print("ancestors of", val)
    while parents[val]:
        print(parents[val], end = "->")
        val = parents[val]


## recursive approach to finding ancestors.
def ancestors_rec(root, key):
    if root is None:
        return 0
    if root:
        if root.val == key:
            return 1
        if ancestors_rec(root.left, key) or ancestors_rec(root.right, key):
            print(root.val)
    else: return 0

tree1 = Node(2)
tree1.left = Node(5) 
tree1.right = Node(6) 
tree1.right.right = Node(7) 
tree1.left.left = Node(8) 

ancestors_rec(tree1, 8)




        






