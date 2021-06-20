from collections import defaultdict
from collections import deque as dq
def solution(n, edge):
    graph = defaultdict(dq)
    for nodes in edge:
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
    print(graph)
    
    nodes = [x for x in range(1, n+1)]
    print(nodes)
    
    # for node in nodes:
    #     visited = dq()
    #     while visited != graph[node]:
    #         start_node = graph[node].popleft()
            
    answer = 0
    return answer