def is_tree(graph):
    if not graph:
        return True

    visited = set()

    def dfs(v, parent):
        visited.add(v)

        for neighbor in graph[v]:
            if neighbor == parent:
                continue

            if neighbor in visited:
                return False

            if not dfs(neighbor, v):
                return False

        return True

    start = next(iter(graph))

    if not dfs(start, None):
        return False

    return len(visited) == len(graph)