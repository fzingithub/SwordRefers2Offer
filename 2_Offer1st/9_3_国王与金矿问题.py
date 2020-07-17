# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 17:32:42 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#简单递归方法 时间空间：O(2^N) 与 M 无关。
class Solution1:
    def __init__(self,G=[],P=[]):
        self.G = G
        self.P = P
        self.N = len(self.G)
        
    def GoldMining(self,N,M): #金矿数量N，人数M; 黄金量列表G， 用工量列表P；
        # write code here
        #定义边界
        if N==1 and M>=self.P[0]:
            return self.G[0]
        if N==1 and 0<=M<self.P[0]:
            return 0
        #定义状态转移 两种情况
        if N>1 and M>=self.P[N-1]:
            return max( self.GoldMining(N-1,M),
                        self.GoldMining(N-1,M-self.P[N-1])+self.G[N-1] )
                       
        if N>1 and M<self.P[N-1]:
            return self.GoldMining(N-1,M)
            

#自底向上 动态规划 时间：O(N*M)  空间：O(M)。
class Solution2:
    def __init__(self,G=[],P=[]):
        self.G = G
        self.P = P
        self.N = len(self.G)
        
    def GoldMining(self,N,M): #金矿数量N，人数M; 黄金量列表G， 用工量列表P；
        # write code here
        preRes = [0]*M
        res = [0]*M
        #只有一个金矿的是时候 
        for i in range(M):
            if i+1<self.P[0]:
                preRes[i] = 0
            else:
                preRes[i] = self.G[0]
        res = preRes.copy()        
                
        for i in range(1,N):
        # 每一层代表前N个金矿人工数（1~10）人的解
        # 前一层已经求出相同人数时选取不同金矿的最大值所以可以叠加
            for j in range(M):
                if (j+1)<self.P[i]:   # j为坐标， j+1为人数
                    res[j] = preRes[j]
                else:
                    tempnum = 0 if j-self.P[i]<0 else j-self.P[i]
                    res[j] =max(preRes[j],preRes[tempnum]+self.G[i])    
            preRes = res.copy()     
        return res[-1]
        
#扩展： 当挖掘工人总数远远大于金矿数量时：N:5， M:1000
#自顶向下递归方法:	时间复杂度  O(2^N)=32	空间复杂度  O(2^5)=32 与M无关
#自底向下迭代方法:	时间复杂度  O(M*N)=5000	空间复杂度	O(M)=1000
#
#所以对于不同问题不总是迭代的时空复杂度由于递归。
           
if __name__ == '__main__':
    test = Solution1([400,500,200,300,350,200,600],[50000,30000,30000,40000,30000,10000,40000])
    res = test.GoldMining(5,100000)