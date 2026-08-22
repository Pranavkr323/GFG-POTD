# GFG POTD - 2026-08-20
# Node and Ancestor Max Diff
# Approach: DFS

''' Structure of Binary Tree Node
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def maxDiff(self, root):
        # Code here 
        ans = float('-inf')

        def dfs(node, max_ancestor):
            nonlocal ans

            if not node:
                return

            ans = max(ans, max_ancestor - node.data)

            max_ancestor = max(max_ancestor, node.data)

            dfs(node.left, max_ancestor)
            dfs(node.right, max_ancestor)

        dfs(root.left, root.data)
        dfs(root.right, root.data)

        return ans
