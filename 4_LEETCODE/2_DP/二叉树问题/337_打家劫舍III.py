class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
在上次打劫完一条街道之后和一圈房屋后，小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为“根”。 除了“根”之外，
每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果两个直
接相连的房子在同一天晚上被打劫，房屋将自动报警。

计算在不触动警报的情况下，小偷一晚能够盗取的最高金额。
'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        if not root:
            return 0

        def _rob(root): # 返回（a, b）当前节点rob时最大数额a, 以及当前节点not_rob时的最大数额b
            if not root:
                return 0, 0

            max_left_rob, max_left_not_rob = _rob(root.left)  # 返回左子树下的 偷与不偷的最大值
            max_right_rob, max_right_not_rob = _rob(root.right)  # 返回右子树下的 偷与不偷的最大值

            rob_get = root.val + max_left_not_rob + max_right_not_rob   # 偷当前节点时 左右子节点只能不偷
            not_rob_get = max(max_right_not_rob, max_right_rob) + max(max_left_not_rob, max_left_rob)  # 不偷当前节点，都可以，取大

            return rob_get, not_rob_get

        return max(_rob(root))


