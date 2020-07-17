class Solution:
    def isBipartite(self, graph):
        n = len(graph)
        UNCOLORED, RED, GREEN = 0, 1, 2
        color = [UNCOLORED] * n
        valid = True

        def dfs(node: int, c: int):
            nonlocal valid
            color[node] = c
            cNei = (GREEN if c == RED else RED)
            for neighbor in graph[node]:
                if color[neighbor] == UNCOLORED:
                    dfs(neighbor, cNei)
                    if not valid:
                        return
                elif color[neighbor] != cNei:
                    valid = False
                    return

        for i in range(n):
            if color[i] == UNCOLORED:
                dfs(i, RED)
                if not valid:
                    break

        return valid




if __name__ == '__main__':
    test = Solution()
    data = [[1],[0],[4],[4],[2,3]]
    res = test.isBipartite(data)

    print(res)