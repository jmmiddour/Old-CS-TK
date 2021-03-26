# from projects.graph.graph import Graph


def earliest_ancestor(ancestors, starting_node):

    # ### Ava's Code ### #
    # lineage = Graph()
    #
    # for parent in ancestors:
    #     if parent[0] not in lineage:
    #         lineage.add_vertex(parent[0])
    #
    #     if parent[1] not in lineage:
    #         lineage.add_vertex(parent[1])
    #
    # paths = lineage.dft_recursive(starting_node)
    #
    # max_len_path = max([len(path) for path in paths]) if len(paths) > 0 else 0
    #
    # possible = []
    #
    # for path in paths:
    #     if len(path) == max_len_path:
    #         possible.append(path)
    #
    # if len(possible) == 1:
    #     return possible[0][-1]
    #
    # elif len(possible) > 1:
    #     current_ancestor = possible[0][-1]
    #
    #     for path in possible:
    #         if path[-1] < current_ancestor:
    #             current_ancestor = path[-1]
    #
    #     return current_ancestor
    #
    # return -1

    # ### Chaz's Code - March 2021 ### #
    from collections import deque

    # Ancestors will be a list of integers in pairs.
    a_dict = {}

    for parent, child in ancestors:
        # print(f'Parent is: {parent}, Child is {child}')
        if child not in a_dict:
            a_dict[child] = set()

        if parent not in a_dict:
            a_dict[parent] = set()

        a_dict[child].add(parent)
        # print(f'Ancestory Dict: {a_dict}')

    q = deque()

    q.append([starting_node])

    max_path = 1
    early = -1

    while q:
        path = q.popleft()
        vert = path[-1]
        # print(f'Path Before if: {path}\nVert Before if: {vert}')

        if (len(path) > max_path) or (len(path) == max_path and vert < early):
            early = vert
            max_path = len(path)
            # print(f'Early in if: {early}\nMax Path in if: {max_path}')

        for conn in a_dict[vert]:
            path_copy = path.copy()
            path_copy.append(conn)
            q.append(path_copy)
            # print(f'Que in for loop: {q}')


if __name__ == '__main__':
    test_ancestors = [(1,3), (2,3), (3,6), (5,6), (5,7), (4,5), (4,8), (8,9),
                      (11,8), (10,1)]

    print(earliest_ancestor(test_ancestors, 6))