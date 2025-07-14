def binary_search_ascii():
    return """Binary Search:
[1, 3, 5, 7, 9]
      ^
Check mid, split left/right, repeat recursively."""

def linear_search_ascii():
    return """Linear Search:
Start -> [1] -> [3] -> [5] -> [7] -> [9] -> End
Check one by one from left to right."""

def dijkstra_ascii():
    return """Dijkstra's Algorithm:
  --1-->   --3-->  
  |                         ^
  \\------4----------------/
Tracks shortest distance from source to all nodes."""

def astar_ascii():
    return """A* Search:
Evaluates f(n) = g(n) + h(n)
where g(n) is cost so far, h(n) is estimated cost.
Used in pathfinding with heuristics."""
