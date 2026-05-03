from collections import deque


def is_bipartite(graph):
    colors = {}

    for start in graph:
        if start not in colors:
            colors[start] = 1
            queue = deque([start])

            while queue:
                vertex = queue.popleft()

                for neighbor in graph[vertex]:
                    if neighbor not in colors:
                        colors[neighbor] = -colors[vertex]
                        queue.append(neighbor)
                    elif colors[neighbor] == colors[vertex]:
                        return False

    return True