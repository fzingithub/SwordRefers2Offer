class Solution:
    def graph_circle_checker(self, graph_string):
        '''
        :param graph_string: {(A->B),(B->C),(C->D)}
        :return: 1 or 0

        BFS 广度优先遍历方法
        时间复杂度 O(m+n)
        空间复杂度 O(m+n)
        '''
        graph = graph_string[1:-1].split(',')
        import collections
        edges = collections.defaultdict(list)  # 邻接表
        indeg = dict()  # 入度
        numCourses = set()

        for info in graph:
            numCourses.add(info[4])
            numCourses.add(info[1])
            edges[info[4]].append(info[1]) # 边 存入 邻接表之中
            if info[1] in indeg:
                indeg[info[1]] += 1  # 被连接节点 入度加一
            else:
                indeg[info[1]] = 1

        q = collections.deque([u for u in list(numCourses) if not indeg])  # 将入度为0的加入队列之中
        visited = 0  # 记录已经遍历的节点数。

        while q:
            visited += 1
            u = q.popleft()
            for v in edges[u]:
                indeg[v] -= 1 # 尾结点入度减一
                if indeg[v] == 0: # 入度为零 加入 队列
                    q.append(v)

        return 0 if  visited == numCourses else 1 # 若 最终遍历的节点数等于总的节点数则不存在环


if __name__ == '__main__':
    test = Solution()

    s = '{(A->B),(B->C),(C->D)}'

    res = test.graph_circle_checker(s)

    print(res)


