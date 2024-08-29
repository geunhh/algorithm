from collections import defaultdict
import math


def check(node, graph):
    if graph[1] == '0':
        return 0

    while node < len(graph) // 2:
        if graph[node] == '0' and (graph[node * 2] == '1' or graph[node * 2 + 1] == '1'):
            return 0
        node += 1
    else:
        return 1


def insert(node, graph, binary_num, index):
    if graph[node] == 0:
        return index

    index = insert(2 * node, graph, binary_num, index)
    graph[node] = binary_num[index]
    index += 1
    index = insert(2 * node + 1, graph, binary_num, index)
    return index


def solution(numbers):
    answer = []

    for N in numbers:
        index = 0
        binary_num = bin(N)[2:]
        graph = defaultdict(int)
        cur_y = len(binary_num)
        h = math.floor(math.log2(cur_y))  # 높이수
        y = 2 ** (h + 1) - 1  # 노드수

        while len(binary_num) < y:
            binary_num = '0' + binary_num

        for i in range(y):
            graph[i + 1] = -1

        insert(1, graph, binary_num, index)
        result = check(1, graph)
        answer.append(result)
    print(answer)

    return answer
solution([7, 42, 5])