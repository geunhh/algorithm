from _collections import defaultdict

L,R=1,2
def insert(tree,node,parent_idx):
    # print(tree,node,parent_idx)
    idx,x,y = node
    (parent_x,parent,y),left,right = tree[parent_idx]

    if parent_idx < x:
        if right != 0:
            insert(tree,node,right)
        else:
            tree[parent_idx][R]=idx
            tree[idx] = [(x,y),0,0]
        print(tree)
    return
    pass

def solution(nodeinfo):
    answer = [[]]
    # y값의 max 값을 찾아.
    sorted_node_info=[]

    for idx,[x,y] in enumerate(nodeinfo,1):
        sorted_node_info.append([idx,x,y])
    # print(sorted_node_info)
    sorted_node_info.sort(key=lambda lst :lst[2])
    print(sorted_node_info) # [idx,x,y]

    tree=defaultdict(list)
    root_idx,root_x,root_y = sorted_node_info.pop()
    tree[root_idx] = [(root_x,root_y),0,0]
    print(tree)
    print(sorted_node_info)

    while sorted_node_info:
        node = sorted_node_info.pop()
        insert(tree,node,root_idx)




inp = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(inp)