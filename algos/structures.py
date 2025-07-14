def bfs_ascii():
    return (
        \"Graph:\\nA — B — C\\n|        |\\nD —— E\\n\\nTraversal: A → B → D → C → E\"
    )

def dfs_ascii():
    return (
        \"Graph:\\nA — B — C\\n|        |\\nD —— E\\n\\nTraversal: A → D → E → C → B\"
    )

def tree_ascii():
    return (
        \"    A\\n   / \\\\n  B   C\\n / \\    \\\\nD   E    F\"
    )

def graph_ascii():
    return (
        \"Graph (adjacency):\\nA: B, D\\nB: A, C\\nC: B, E\\nD: A, E\\nE: C, D\"
    )

def hashtable_ascii():
    return (
        \"Hashtable:\\nIndex 0: —\\nIndex 1: apple\\nIndex 2: banana\\nIndex 3: —\\nIndex 4: cat\\nCollision handled by chaining\"
    )

def stack_ascii():
    return (
        \"Stack:\\nTop → [9, 7, 3]\\nPush(5) → [5, 9, 7, 3]\\nPop() → 5\\nNow → [9, 7, 3]\"
    )

def queue_ascii():
    return (
        \"Queue:\\nFront → [2, 4, 6]\\nEnqueue(8) → [2, 4, 6, 8]\\nDequeue() → 2\\nNow → [4, 6, 8]\"
    )
