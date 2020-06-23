import cProfile
from graph_goody import random_graph, spanning_tree
import pstats

# Put script below to generate data for Problem #2
# In case you fail, the data appears in sample8.pdf in the helper folder
def multby10(x:int) -> int:
    return x*10
r1 = random_graph( 5000, multby10)
r2 = random_graph(10000, multby10)
cProfile.run('spanning_tree(r1)', 'profile')
p = pstats.Stats('profile')
#p.str_dirs().sort_stats(-1).print_stats()
p.sort_stats('calls').print_stats()
cProfile.run('spanning_tree(r2)', 'profile')
p = pstats.Stats('profile')
p.sort_stats('tottime').print_stats()