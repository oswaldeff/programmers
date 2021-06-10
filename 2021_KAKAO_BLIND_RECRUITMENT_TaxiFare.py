from collections import defaultdict
def solution(n, s, a, b, fares):
    graph_fare = {}
    graph_node = {}
    for i in range(n):
        graph_fare[i+1] = defaultdict(int)
        graph_node[i+1] = list()
    
    for fare in fares:
        graph_fare[fare[0]][fare[1]] = fare[2]
        graph_fare[fare[1]][fare[0]] = fare[2]
        graph_node[fare[0]].append(fare[1])
        graph_node[fare[1]].append(fare[0])
    
    print('graph_fare: ', graph_fare)
    print('graph_node: ', graph_node)
    answer = 0
    return answer
