'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
'''
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        # this is the dfs approach also look into the bfs and recursive approach
        height = 0
        q  = []
        if root:
            q.append(root)
        while len(q) > 0:
            for i in range(len(q)):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            height += 1
        return height
