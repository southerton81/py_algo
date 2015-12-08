from heapq import heappush, heappop

#Priority queue that checks whether item is already added and "removes" it in such case
import sys


class PriorityQueue:
    def __init__(self):
        self.pq = []                         # list of entries arranged in a heap
        self.entry_finder = {}               # mapping of tasks to entries
        self.REMOVED = -1                    # placeholder for a removed task

    def add_vertex(self, vertex, priority):
        'Add a new vertex or update the priority of an existing'
        if vertex in self.entry_finder:
            self.remove_vertex(vertex)
        entry = [priority, vertex]
        self.entry_finder[vertex] = entry
        heappush(self.pq, entry)

    def remove_vertex(self, vertex):
        'Mark an existing vert as REMOVED.  Raise KeyError if not found.'
        entry = self.entry_finder.pop(vertex)
        entry[-1] = self.REMOVED

    def pop_vertex(self):
        'Remove and return the lowest priority task. Raise KeyError if empty.'
        while self.pq:
            item = heappop(self.pq)
            priority, vertex = item
            if vertex is not self.REMOVED:
                del self.entry_finder[vertex]
                return vertex
        return -1

class Graph(object):
    def __init__(self):
        self.graph = [[]]

        while len(self.graph) < 200:
            self.graph.append([])

        with open("data/dijkstraData.txt") as f:
            for line in f:
                line = line.rstrip()
                line = line.split('\t')
                vertex = int(line[0])
                while len(self.graph) - 1 < vertex:
                    self.graph.append([])

                for child_index in range(1, len(line)):
                    child_line = line[child_index]
                    child_line = child_line.split(',')
                    # child_line[1] = distance to child from vertex, child_line[0] = child name
                    self.graph[vertex].append((int(child_line[1]), int(child_line[0])))

    def get_vertex(self, i):
        return self.graph[i]

    def get_vertex_range(self):
        return range(1, len(self.graph))


def dijkstra(graph, source):
    INFINITY = sys.maxsize
    dist = {}

    verts = graph.get_vertex_range()
    for v in verts:
        dist[v] = INFINITY

    dist[source] = 0
    Q = PriorityQueue()
    Q.add_vertex(source, dist[source])

    u = Q.pop_vertex()
    while u is not -1:
        neighbours = graph.get_vertex(u)
        for v in neighbours:
            alt = dist[u] + v[0] # v[0] = dist(u, v)
            v_name = v[1]
            if alt < dist[v_name]:
                dist[v_name] = alt
                Q.add_vertex(v_name, alt)
        u = Q.pop_vertex()
    return dist

g = Graph()
distances = dijkstra(g, 1)


print(distances[7],
distances[37],
distances[59],
distances[82],
distances[99],
distances[115],
distances[133],
distances[165],
distances[188],
distances[197], sep = ",")