
# Graph representation:
#                   vertex 1   vertex2      vn
# list of lists [[][1,2,3,4], [34,32,1] ... []]
import operator
import time
from functools import reduce

leaders = {}

def read_from_file(fname):
    graph = [[]]
    with open(fname) as f:
        for line in f:
            line = line.rstrip()
            line = line.split(' ')
            v1 = int(line[0])
            v2 = int(line[1])

            while len(graph) - 1 < v1:
                graph.append([])

            graph[v1].append(v2)
    return graph

def unvisited_childs_exists(childs, visited):
    for child in childs:
        if child not in visited:
            return True
    return False

def dfs(graph, start_node, visited, t, f, set_leaders):
    stack = [start_node]
    route = []

    while (stack):
        node = stack.pop()

        if node in visited:
            continue
        visited.add(node)

        if (set_leaders):
            leaders[node] = start_node

        route.append(node)
        adjastent = graph[node]
        adjastent = [n for n in adjastent if n not in visited]
        if not adjastent:
            while (route):
                node = route[-1]
                node_childs = graph[node]

                if unvisited_childs_exists(node_childs, visited):
                    break

                route.pop()
                t += 1
                f[node] = t

        stack.extend(adjastent)

    return t


# The second path must always start from sink vertex that is determined on first pass
# That's the whole point. Otherwise we would need to test each vertex with dfs.
# start_from_sink_vertex added just to emphasize the need to start from newly labeled
# sink vertex on second pass, though first search may start from any vertex.
# It really doesn't matter which node you start from, on original graph to get finish time of nodes.
def dfs_loop(graph, set_leaders, start_from_sink_vertex):
    f = {}
    t = 0
    vertex_count = len(graph)
    visited = set()

    rng = range(1, vertex_count)
    if start_from_sink_vertex : rng = reversed(rng)

    for i in rng:
        if i in visited : continue
        t = dfs(graph, i, visited, t, f, set_leaders)

    #print(f)
    return f


def reverse_graph(graph):
    reversed_graph = [[] for i in range(len(graph))]
    vertex_count = len(graph)
    for i in range (1, vertex_count):
        adjastent = graph[i]
        for a in adjastent:
            reversed_graph[a].append(i)
    return reversed_graph

def change_graph_labels_to_f(f, graph):
    labeled_graph = [[] for i in range(len(graph))]

    #print (labeled_graph)
    for key, value in f.items():
        old_label = key
        new_label = value
        adjustent = list(graph[old_label])
        for a in adjustent:
            labeled_graph[new_label].append(f[a])
    return labeled_graph

# checks to see whether there are vertices that are not added to the graph
# because they don't have any outbound edges, but only inbound ones
def test_graph(graph):
    flat_graph = [item for sublist in graph for item in sublist]
    max_vertex = reduce(max, flat_graph)
    print ('max vertex index ' + str(reduce(max, flat_graph)))
    if len(graph) <= max_vertex:
        print ('vertex ' + str(max_vertex) + ' not in graph, appending')
        while len(graph) <= max_vertex:
            graph.append([])


print ('Loading graph')


#read_file_time = int(round(time.time() * 1000))
graph = read_from_file('Data/testgraph_for_strong_comp')
#print (str(int(round(time.time() * 1000) - read_file_time)))

test_graph(graph)

print ('Reversing graph')

#algo_time = int(round(time.time() * 1000))

reversed_graph = reverse_graph(graph)

print ('DFS on reversed graph')
f = dfs_loop(reversed_graph, set_leaders=False, start_from_sink_vertex=False)

relabled_graph = change_graph_labels_to_f(f, graph)
f = dfs_loop(relabled_graph, set_leaders=True, start_from_sink_vertex=True)

loop_counter = {}
for value in leaders.values():
    if value in loop_counter:
        loop_counter[value] += 1
    else:
        loop_counter[value] = 1

sorted_loop_counter = sorted(loop_counter.items(), key=operator.itemgetter(1), reverse=True)

acc = 1
for x in sorted_loop_counter:
    print (x[1])
    acc += 1
    if acc == 6: break


print ('Completed')
