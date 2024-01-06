from graphviz import Digraph

from btree import BPlusTree
import uuid

btree = BPlusTree(3)

elements = [
    3,
    2,
    1,
    4,
    10,
    11,
    34,
    120,
    128,
    39,
    190,
    42,
    200,
    201,
    203,
    5,
    6,
    7,
    8
]


for element in elements:
    btree.insert(element)
    print(btree.height)
    print(btree)

print("b plus tree")
print(btree)


    
def visualize_btree(btree):
    graph = Digraph(comment="BPlusTree")
    graph.attr(rankdir="TB", splines="true", nodesep="0.5", ranksep="0.5")
    level = [btree.root]
    link = None
    while level:
        with graph.subgraph() as s:
            s.attr(rank='same')
            for node in level:
                s.node(node.id, str(node.keys)) 
        if not level[0].children:
            link = level[0]
            while link.next_node:
                graph.edge(link.id, link.next_node.id)
                link = link.next_node
                
        new_level = []
        for item in level:
            for child in item.children:
                new_level.append(child)
                graph.edge(item.id, child.id)

        level = new_level
    
    return graph

    
visualize_btree(btree).view()


