from performance import Performance
from goody import irange
from graph_goody import random_graph,spanning_tree

# Put script below to generate data for Problem #1
# In case you fail, the data appears in sample8.pdf in the helper folder

def multby10 (x: int) -> int:
    return x * 10

random_graph(8, multby10)
print (random_graph(8, multby10))
for x in range(8):
    nodes = 1000 * (2 ** x)
    print (nodes)
    def create_random():
        return random_graph(nodes, multby10)
    def spamming_tree():
        return spanning_tree(create_random())
    p = Performance(spamming_tree, create_random, 5, 'spanning tree of size ' + str(nodes))
    p.evaluate()
    p.analyze()
print ("Done")