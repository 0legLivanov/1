import networkx as nx
import matplotlib.pyplot as plt
import random
graph = nx.Graph()
x = 'ABCDERTYNVSLKHPOQW'
o = random.randint(4, 7)
c = random.choices(x, k=o)
for i in c:
    graph.add_node(i)
for i in range(o):
    graph.add_edge(c[0], c[o-random.randint(1, o-1)])
    graph.add_edge(c[0], c[o-random.randint(1, o-1)])
    graph.add_edge(c[1], c[o-random.randint(1, o-1)])
    graph.add_edge(c[1], c[o-random.randint(1, o-1)])
nx.draw(graph, with_labels=True)
pos = nx.spring_layout(graph)
edge_weight = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_weight)
plt.show()
