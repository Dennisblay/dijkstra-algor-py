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
