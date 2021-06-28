from collections import defaultdict
from collections import deque as dq
def solution(n, edge):
    graph = defaultdict(dq)
    for nodes in edge:
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
    print(graph)
    
    nodes = [x for x in range(1, n+1)]
    offset = None
    limit = None
    print(nodes[offset:limit])
    
    for node in nodes:
        visited = []
        while True:
            present_node = int(node)
            visited.append(present_node)
            previous_node = int(present_node) 
            present_node = graph[present_node].popleft()
            if len(graph[present_node]) > 0:
                graph[previous_node].appendleft(present_node)
            visited.append(present_node)
            
            
    answer = 0
    return answer