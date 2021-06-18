from collections import defaultdict
def solution(n, edge):
    graph = defaultdict(list)
    for nodes in edge:
        graph[nodes[0]].append(nodes[1])
        graph[nodes[1]].append(nodes[0])
    print(graph)
    answer = 0
    return answer