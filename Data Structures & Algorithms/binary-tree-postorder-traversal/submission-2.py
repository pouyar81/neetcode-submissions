# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        stack = [root]
        visited = [False]
        result = []

        while stack:
            current, visit = stack.pop(), visited.pop()
            if current:
                if visit:
                    result.append(current.val)
                else:
                    stack.append(current)
                    visited.append(True)
                    stack.append(current.right)
                    visited.append(False)
                    stack.append(current.left)
                    visited.append(False)

        return result
        