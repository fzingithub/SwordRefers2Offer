class Solution:
    def verifyPostorder(self, postorder: 'List[int]') -> bool:
        if not postorder:
            return True

        rootVal = postorder[-1]

        firstGreaterIdx = 0
        while postorder[firstGreaterIdx] < rootVal:
            firstGreaterIdx += 1

        for num in postorder[firstGreaterIdx:-1]:
            if num < rootVal:
                return False

        return self.verifyPostorder(postorder[:firstGreaterIdx]) and self.verifyPostorder(postorder[firstGreaterIdx:-1])