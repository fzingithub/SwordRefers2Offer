n = int(input())

graph = []
for i in range(n):
    graph.append(input().split())

# print(graph)
S = list(set(sum(graph, [])))
# print(S)

HasMap = dict()
for i in range(len(S)):
    HasMap[S[i]] = str(i)
# print(HasMap)

child_graph = dict()
for i in range(len(S)):
    child_graph[str(i)] = ''

# print(child_graph)
for ele in graph:
    child_graph[HasMap[ele[0]]] = str(HasMap[ele[1]]) if child_graph[HasMap[ele[0]]]=='' else child_graph[HasMap[ele[0]]]+'#'+ str(HasMap[ele[1]])
# print(child_graph)


visited = []
trace = []
has_circle = False
res = 0

def dfs(node_index):
    global has_circle, res
    if (node_index in visited):
        if (node_index in trace):
            has_circle = True
            trace_index = trace.index(node_index)
            # for i in range(trace_index, len(trace)):
            #     print(trace[i] + ' ', end='')
            # print('\n', end='')
            res += 1
            return
        return

    visited.append(node_index)
    trace.append(node_index)

    if (node_index != ''):
        children = child_graph[node_index].split('#')
        for child in children:
            dfs(child)
    trace.pop()


dfs("京东")
print(res)
if (has_circle == False):
    print("No Cycle.")