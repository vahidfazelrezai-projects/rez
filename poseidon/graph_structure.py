# poseidon graph structure
#
# directed graph where vertices are strings and edges consist of a start vertex,
# an end vertex, and a relationship (represented as a string)

rel_words = ['is', 'was', 'will be', 'isn\'t', 'is not', 'wasn\'t', 'was not', 'won\'t be', 'will not be']

class Graph():

    def __init__(self):
        self.vertices = []
        self.edges = []

    def __str__(self):
        return 'Vertices: ' + str(self.vertices) + '\nEdges: ' + str(self.edges)

    # edge is of type Edge
    def add_edge(self, edge):
        if edge.start not in self.vertices:
            self.vertices.append(edge.start)

        if edge.end not in self.vertices:
            self.vertices.append(edge.end)

        self.edges.append(edge)


class Vertex():

    # key is a string
    def __init__(self, key):
        self.key = key

    def __str__(self):
        return self.key

    def key(self):
        return self.key


class Edge():

    # start and end are of type Vertex, rel is a string
    def __init__(self, start, end, rel):
        self.start = start
        self.end = end
        self.rel = rel

    def __str__(self):
        return str(self.start) + ' ' + self.rel + ' ' + str(self.end)

    def start(self):
        return self.start

    def end(self):
        return self.end

    def rel(self):
        return self.rel


def call(inp):
    return inp
