def bfs_ascii():
    return """Breadth-First Search:
Start -> [A]
         |\\
        [B][C]
         |\\
        [D][E]
Traverse level by level."""

def dfs_ascii():
    return """Depth-First Search:
Start -> [A]
          |
         [B]
          |
         [D]
Backtrack then -> [E] -> [C]
Explore as deep as possible first."""

def tree_ascii():
    return """Binary Tree:
       [10]
      /    \\
    [5]    [15]
   /  \\
 [2]  [7]"""

def graph_ascii():
    return """Graph:
[A] -- [B] -- [C]
 |      |
[D] -- [E]
Arbitrary connections between nodes."""

def hashtable_ascii():
    return """Hash Table:
+----+--------+
|  0 |   None |
|  1 |   15   |
|  2 |   7    |
+----+--------+
Key-value storage with fast lookup."""

def stack_ascii():
    return """Stack (LIFO):
|   5   |
|   4   |
|   3   |
 -------
Push and pop from the top only."""

def queue_ascii():
    return """Queue (FIFO):
[3] -> [4] -> [5] ->
First in, first out processing."""

def avl_tree_ascii():
    return """AVL Tree (Balanced BST):
       [30]
      /    \\
    [20]   [40]
   /          \\
 [10]         [50]
Auto-balances after insertions/deletions."""
