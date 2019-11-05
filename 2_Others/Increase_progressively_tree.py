# -*- coding: utf-8 -*-
'''
Created on 2019/9/7
Author: zhe
Email: 1194585271@qq.com
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# 层次打印二叉树
def Print(pRoot):
    # write code here
    if not pRoot:
        return []
    if not pRoot.left and not pRoot.right:
        return [[pRoot.val]]
    stack = [pRoot]
    output = []
    while (stack):
        temp = []
        for i in range(len(stack)):
            out_node = stack.pop(0)
            temp.append(out_node.val)
            if out_node.left is not None:
                stack.append(out_node.left)
            if out_node.right is not None:
                stack.append(out_node.right)
        output.append(temp)
    return output

import sys

lines = sys.stdin.readlines()

T = int(lines[0].strip().split()[0])   #T>=0

numLine = 1
for i in range(T):
    N = int(lines[numLine].strip().split()[0])
    numLine += 1
    nodes = lines[numLine:numLine+N]
    numLine += N
    nodesInt = []
    for line in nodes:
        nodesInt.append(list(map(int, line.strip().split())))

    #创建树节点
    nodesTree = []
    for i in range(N):
        nodesTree.append(TreeNode(nodesInt[i][0]))

    #创建树
    for i in range(N):
        if nodesInt[i][1] == -1:
            nodesTree[i].left = None
        else:
            nodesTree[i].left = nodesTree[nodesInt[i][1]]
        if nodesInt[i][2] == -1:
            nodesTree[i].right = None
        else:
            nodesTree[i].right = nodesTree[nodesInt[i][2]]

    # 寻找头结点
    ListToSet = []
    for i in range(N):
        ListToSet.extend(nodesInt[i][1:])
    rootNum = list(set(range(-1,N)) ^ set(ListToSet))[0]
    root = nodesTree[rootNum]   # 树头结点

    layerTras = Print(root) # 层次遍历打印多行

    layerSum = list(map(sum, layerTras)) #每层和
    # print(layerTras)
    # print(layerSum)
    # print (rootNum)

    mark = True
    for i in range(len(layerSum)-1):
        if layerSum[i]>=layerSum[i+1]:
            print('NO')
            mark = False
            break

    if mark == True:
        print('YES')


# 示例
# 2
# 8
# 2 -1 -1
# 1 5 3
# 4 -1 6
# 2 -1 -1
# 3 0 2
# 2 4 7
# 7 -1 -1
# 2 -1 -1
# 8
# 21 6 -1
# 52 4 -1
# 80 0 3
# 31 7 -1
# 21 -1 -1
# 59 -1 -1
# 50 5 -1
# 48 -1 1