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

    steps.append("📘 BFS Traversal\n")
    steps.append("Start from node: A\n")

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            steps.append(f"→ Visited: {node}")
            if graph[node]:
                steps.append(f"   Enqueue neighbors of {node}: {', '.join(graph[node])}")
            else:
                steps.append(f"   No neighbors to enqueue for {node}")
            queue.extend(graph[node])

    steps.append("\n✅ Final Traversal Order:")
    steps.append(" → ".join(visited))
    return "\n\n".join(steps)


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
            steps.append(f"→ Visited: {node}")
            for neighbor in graph[node]:
                steps.append(f"   Recurse to: {neighbor}")
                dfs(neighbor)

    steps.append("📘 DFS Traversal\n")
    steps.append("Start from node: A\n")
    dfs('A')

    steps.append("\n✅ Final Traversal Order:")
    steps.append(" → ".join(visited))
    return "\n\n".join(steps)
