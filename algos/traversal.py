def bfs_steps():
    steps = []
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    queue = ['A']
    visited = []

    steps.append("BFS traversal starting from A")
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            steps.append(f"Visited {node}")
            queue.extend(graph[node])
    steps.append(f"Traversal order: {' → '.join(visited)}")
    return "\n".join(steps)


def dfs_steps():
    steps = []
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    visited = []

    def dfs(node):
        if node not in visited:
            visited.append(node)
            steps.append(f"Visited {node}")
            for neighbor in graph[node]:
                dfs(neighbor)

    steps.append("DFS traversal starting from A")
    dfs('A')
    steps.append(f"Traversal order: {' → '.join(visited)}")
    return "\n".join(steps)
