# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""Module"""
class Solution:
    """class"""
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        """delete node"""
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)

        if key < root.val:
            root.left = self.deleteNode(root.left, key)


        if key == root.val:
            #1
            if not root.left and not root.right:
                return None
            #2
            if root.right and root.left:
                successor = root.right
                while successor.left:
                    successor = successor.left

                root.val = successor.val
                root.right = self.deleteNode(root.right, successor.val)

            #3
            elif root.right or root.left:
                if root.right:
                    return root.right
                if root.left:
                    return root.left
        return root
