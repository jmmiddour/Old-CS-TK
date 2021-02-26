from CS07_Graphs.projects.graph.graph import Graph


def earliest_ancestor(ancestors, starting_node):
    lineage = Graph()

    for parent in ancestors:
        if parent[0] not in lineage:
            lineage.add_vertex(parent[0])

        if parent[1] not in lineage:
            lineage.add_vertex(parent[1])

    paths = lineage.dft_recursive(starting_node)

    max_len_path = max([len(path) for path in paths]) if len(paths) > 0 else 0

    possible = []

    for path in paths:
        if len(path) == max_len_path:
            possible.append(path)

    if len(possible) == 1:
        return possible[0][-1]

    elif len(possible) > 1:
        current_ancestor = possible[0][-1]

        for path in possible:
            if path[-1] < current_ancestor:
                current_ancestor = path[-1]

        return current_ancestor

    return -1