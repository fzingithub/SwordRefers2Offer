import collections
class Solution:
    def canFinish(self, numCourses: int, prerequisites: 'List[List[int]]') -> bool:
        '''
        BFS 广度优先遍历
        时间复杂度 O(m+n)
        空间复杂度 O(m+n)
        '''
        edges = collections.defaultdict(list)      # 邻接表
        indeg = [0] * numCourses  # 入度

        for info in prerequisites:
            edges[info[1]].append(info[0]) # 边 存入 邻接表之中
            indeg[info[0]] += 1  # 被连接节点 入度加一

        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])    # 将入度为0的加入队列之中
        visited = 0 # 记录已经遍历的节点数。

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1 # 尾结点入度减一
                if indeg[v] == 0: # 入度为零 加入 队列
                    q.append(v)

        return visited == numCourses # 若 最终遍历的节点数等于总的节点数则不存在环

    def canFinish1(self, numCourses: int, prerequisites: 'List[List[int]]') -> bool:
        '''
        DFS 深度优先遍历 较难理解
        每个节点有三种状态 0:未搜索；京东：搜索中；2：搜索完毕
        '''
        edges = collections.defaultdict(list) # 邻接表存储
        visited = [0] * numCourses # 是否访问过
        result = list() # 结果集
        valid = True # 是否存在环

        for info in prerequisites: # 存入邻接表
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1 # 节点 u 搜索中
            for v in edges[u]:
                if visited[v] == 0: # 未搜索
                    dfs(v) # 深度优先
                    if not valid: # 存在环
                        return # 返回
                elif visited[v] == 1: # 子节点 在搜索中状态 一定存在环
                    valid = False # 存在环
                    return #返回
                else: # 如果该子节点被遍历过， 什么也不干
                    pass
            visited[u] = 2 # 递归遍历完 设置为 2
            result.append(u) # 加入 拓扑排序结果集

        for i in range(numCourses):
            if valid and not visited[i]: # 如果 不存在环，且该节点未被搜索，进行深度优先搜索
                dfs(i)
        print(result[::-1])
        return valid # 返回是否存在环

if __name__ == '__main__':
    test = Solution()

    n, L = 7, [[0, 2], [0, 4], [0, 5], [1, 0], [1, 2], [3, 5], [5, 4], [5, 6]]
    # n, L = 2, [[1, 0]]

    res = test.canFinish(n, L)

    print(res)