class TreeNode:
    def __init___(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def sortedArr2BST(self, nums):
        if not nums:
            return None

        mid = len(nums)//2

        pNode = TreeNode(nums[mid])
        pNode.left = self.sortedArr2BST(nums[:mid])
        pNode.right = self.sortedArr2BST(nums[mid+1:])

        return pNode
