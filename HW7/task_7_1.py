def has_cycle(graph):
    visited = set()

    def dfs(v, parent):
        visited.add(v)

        for neighbor in graph[v]:
            if neighbor == parent:  # eсли это путь назад -- пропускаем
                continue

            if neighbor in visited: # eсли это уже посещённая вершина -- нашли цикл
                return True

            if dfs(neighbor, v):  # eсли ещё не посещали -- идём туда глубже.
                return True

        return False

    for vertex in graph:
        if vertex not in visited:  #eсли мы в ней ещё не были -- начинаем из неё обход (DFS).
            if dfs(vertex, None): # eсли во время обхода нашли цикл -- сразу заканчиваем и говорим, что цикл есть
                return True

    return False