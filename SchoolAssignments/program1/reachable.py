# Submitter: nschultz(Schultz-Cox, Neil)
# Partner  : kthirano(Hirano, Kohsuke)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming


import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    graph_dictionary = defaultdict(set)
    graph_list = []
    file = file.readlines()
    for node in range(0, len(file)):
        file[node] = file[node].strip()
        graph_list.append(file[node].split(';'))
    for k, v in graph_list:
        graph_dictionary[k].add(v)
    return graph_dictionary


def graph_as_str(graph : {str:{str}}) -> str:
    graph_string = ''
    for k, v in sorted(graph.items(), key=lambda x : x[0]):
        graph_string += ('  ' + k + ' ' + '->' + ' ' + str(sorted(v)) + '\n')
    return graph_string

        
def reachable(graph : {str:{str}}, start : str) -> {str}:
    masterlist = set()
    remaining_dict = graph
    if start in graph or start in graph.values():
        masterlist.add(start)
        del remaining_dict[start]
    templist = graph.get(start)
    if templist != None:
        for items in templist:
            x = reachable(remaining_dict, items)
            if len(x) != 0:
                for r in x:
                    masterlist.add(r)
                    del remaining_dict[r]
            else:
                masterlist.add(items)
                del remaining_dict[items]
                
    return masterlist 


if __name__ == '__main__':
    # Write script here
    graph_path = open(input('Enter some graph file name: '))
    final_dictionary = read_graph(graph_path)
    print()
    print('Graph: source node -> [destination nodes]')
    print(graph_as_str(final_dictionary))
    
    while True:
        start_node = input('Enter some starting node name (else quit): ')
        if start_node == 'quit':
            break
        else:
            reach = reachable((final_dictionary), start_node, [])
            if len(reach) == 0:
                print ("  Entry Error: '" + start_node + "'; Illegal: not a source node")
                print ("  Please enter a legal String")
            else:
                print ("  From " + start_node + " the reachable nodes are " + str(reach))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
