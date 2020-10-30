'''
方法：最短路径方法：floyd算法。
这里采用的是floyd而非Dijkstra，是因为要求任意两节点之间的最短路径。
假设无向图关系网中的权值均为1，则利用floyd算法求得的任意两两之间的最短路径中取最大值为max_num。
则结果res = max_num，res则为最终结果，此社交网络为res度分割网络。

无向图利用邻接矩阵表示 dis，节点总数为n。
代码见下方代码区。

时间复杂度分析， floyd算法核心是三层循环因此时间复杂度为 O(n^3)。
空间复杂度分析， 借助邻接矩阵来表示关系网，空间复杂度为 O(n^2)。
其中n为节点个数，也就是数据规模。
'''

class Solution:
    def floyd(dis, n):
        '''
        :param dis:  邻接矩阵
        :param n:  节点数
        :return: 原地返回 dis
        '''
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    new_distance = dis[i][k] + dis[k][j]  # 查看是否有更短的捷径
                    if new_distance<dis[i][j]:
                        dis[i][j] = new_distance
        return dis

    def NDimensionSpace(self, dis, n):
        dis = self.floyd(dis, n)
        res = max(map(max, dis))
        return res
