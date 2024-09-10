tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
from _collections import defaultdict

def dfs(graph):
    pass


def solution(tickets):
    answer = []
    graph = defaultdict(list)
    for s,e in tickets:
        graph[s].append(e)

    print(graph)
    for s in graph:
        graph[s].sort() # key값으로 불러와서 sort해줌.
    print(graph)
    graph['ICN'].remove(graph['ICN'][0])
    print(graph)
    graph['ICN'].remove(graph['ICN'][0])
    print(graph)
    for dd in graph:
        if graph[dd] == []:
            continue
        else:
            print('gg')




    return answer

solution(tickets)