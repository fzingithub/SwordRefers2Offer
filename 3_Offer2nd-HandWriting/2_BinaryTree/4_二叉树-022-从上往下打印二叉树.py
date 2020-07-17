class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Soluton:
    def PrintFromTopToBottom(self, pRoot):
        '''
        借助队列
        :param pRoot:
        :return: List
        '''

        if not pRoot:
            return []

        Queue = [pRoot]
        res = []

        while Queue:
            pNode = Queue.pop(0)
            res.append(pNode.val)
            if pNode.left:
                Queue.append(pNode.left)
            if pNode.right:
                Queue.append(pNode.right)

        return res
