import math

def findCycles(nodes, adjacencyList, u):
    queue = [u]
    FOUND = False
    distance_u = dict(zip(nodes, [math.inf]*len(nodes)))
    distance_u[u] = 0
    parent = dict(zip(nodes, [-1]*len(nodes)))
    visited = dict(zip(nodes, [False]*len(nodes)))
    parent[u] = u
    path = []
    visited[u] = True
    while len(queue) > 0 and not FOUND:
        node = queue[-1]
        del(queue[-1])
        for v in adjacencyList[node]:
            if v == u:
                FOUND = True
                length = distance_u[node] + 1
                p=node
                path.append(u)
                while p!=u:
                    path.append(p)
                    p = parent[p]
                path.append(u)
                break
            else:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    distance_u[v] = distance_u[node]+1
                    parent[v] = node
        path.reverse()
    return (True, length, path) if FOUND else (False, -1, path)

adjacencyList = {1:[2], 2:[3], 3:[4], 4:[5,6,2], 5:[2], 6:[]}
print(findCycles([1,2,3,4,5,6], adjacencyList, 2))
