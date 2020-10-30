import collections
def findOrder(numCourses, prerequisites):
    edges = collections.defaultdict(list)
    indeg = [0] * numCourses  # 入度
    ans = []

    for info in prerequisites:
        edges[info[1]].append(info[0])
        indeg[info[0]] += 1

    q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
    visited = 0

    while q:
        visited += 1
        u = q.popleft()
        ans.append(u)
        for v in edges[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)

    return ans if visited == numCourses else []

nums = list(map(int, input().split(',')))
n = len(nums)
edges = []
for i in range(n):
    if nums[i] != -1:
        edges.append([i, nums[i]])

ans = findOrder(n, edges)
print(','.join(map(str,ans)))
'''
1,2,-1,1
'''