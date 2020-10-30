# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def __init__(self):
        self.visited = {}  # dict

    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        DFS
        '''
        if not node:
            return node

        #如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回。
        if node in self.visited:
            return self.visited[node]

        # 克隆节点， 注意为了深拷贝， 我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

    def cloneGraph(self, node: 'Node') -> 'Node':
        '''
        BFS
        '''

        if not node:
            return node

        visited = {}

        queue = [node]

        visited[node] = Node(node.val, [])

        while queue:
            element_node = queue.pop()  #取出节点
            for neighbor_node in element_node.neighbors: #遍历邻居节点
                if not neighbor_node in visited: # 若该邻居节点的clone节点没被被创建过
                    visited[neighbor_node] = Node(neighbor_node.val, [])    # 先创建
                    queue.append(neighbor_node)  # 为创建过 加入队列中 否则不加入队列 避免循环
                visited[element_node].neighbors.append(visited[neighbor_node])   # 加入到clone节点的邻居列表中

        return visited[node]

