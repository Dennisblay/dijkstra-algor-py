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
