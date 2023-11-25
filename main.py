from collections import defaultdict


class Graph(object):

    def __init__(self):
        """
               self.edges is a dict of all possible next nodes
               e.g. {'X': ['A', 'B', 'C', 'E'], ...}
               self.weights has all the weights between two nodes,
               with the two nodes as a tuple as the key
               e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
               """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_node(self, from_node, to_node, weight):
        # Note: assumes edges are bi-directional
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = weight


new_graph = Graph()

edges = [
    ('X', 'A', 7),
    ('X', 'B', 2),
    ('X', 'C', 3),
    ('X', 'E', 4),
    ('A', 'B', 3),
    ('A', 'D', 4),
    ('B', 'D', 4),
    ('B', 'H', 5),
    ('C', 'L', 2),
    ('D', 'F', 1),
    ('F', 'H', 3),
    ('G', 'H', 2),
    ('G', 'Y', 2),
    ('I', 'J', 6),
    ('I', 'K', 4),
    ('I', 'L', 4),
    ('J', 'L', 1),
    ('K', 'Y', 5),
]

for edge in edges:
    new_graph.add_node(*edge)

print(new_graph.edges)

def dijkstra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    # visited is a set()
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    # While the current node is not equal to the end node
    # Add current node the visited nodes set
    # Get all possible destinations of current node from the shortest_paths dict
    # Get the weight to the current node to the prev node

    # for next_node in destinations:
    # compute the next weight given the prev weight
    # Update shortest_path dict, else
    #



