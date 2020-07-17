class TreeNode:
    def __int__(self, value):
        self.val = value
        self.left = None
        self.right = None

class Solution:
    def Serialize(self, pRoot):
        if not pRoot:
            return '#'

        return str(pRoot.val) + '!' + self.Serialize(pRoot.left) + '!' + self.Serialize(pRoot.right)


    def Deserialize(self, strSerialize):
        if not strSerialize:
            return None

        serializeList = strSerialize.split('!')

        return self.DeserializeTree(serializeList)

    def DeserializeTree(self, serializeList):
        if not serializeList:
            return None

        value = serializeList.pop(0)
        pNode = None
        if value != '#':
            pNode = TreeNode(int(value))
            pNode.left = self.DeserializeTree(serializeList)
            pNode.right = self.DeserializeTree(serializeList)

        return pNode
