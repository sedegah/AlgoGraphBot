# AlgoGraphBot

**AlgoGraphBot** is a Telegram bot that visualizes common algorithms and data structures as ASCII or text-based flows. It's designed for students, educators, and developers who want quick visual insights into how sorting, searching, recursion, and structural operations work — right from Telegram.

---

## Features

AlgoGraphBot supports visual explanations for:

###  Sorting Algorithms

* `/bubble` – Bubble Sort
* `/selection` – Selection Sort
* `/insertion` – Insertion Sort
* `/quick` – Quick Sort

###  Searching Algorithms

* `/linear` – Linear Search
* `/binary` – Binary Search

###  Recursion Traces

* `/factorial` – Factorial Function Trace
* `/fibonacci` – Fibonacci Function Trace

###  Data Structures

* `/tree` – Binary Tree (ASCII view)
* `/graph` – Adjacency Representation
* `/bfs` – Breadth-First Search
* `/dfs` – Depth-First Search
* `/hashtable` – Hash Table with Chaining
* `/stack` – Stack Operations (Push/Pop)
* `/queue` – Queue Operations (Enqueue/Dequeue)

---

## Bot Overview

* **Framework**: Python 3.11

* **Libraries**:

  * `python-telegram-bot` (v20.7)
  * `FastAPI` for webhook integration
  * `uvicorn` for serving the FastAPI app

* **Structure**:

```
algographbot/
├── api/
│   └── webhook.py         # Telegram-FastAPI bridge
├── algos/                 # Visual algorithm implementations
│   ├── sorting.py
│   ├── searching.py
│   ├── recursion.py
│   └── structures.py
├── requirements.txt
└── runtime.txt
```

## Example Commands

```
/start         → Welcome message
/bubble        → Step-by-step Bubble Sort
/quick         → Quick Sort partitioning view
/factorial     → Recursive factorial breakdown
/dfs           → DFS traversal in a graph
/stack         → Stack push/pop transitions
```


## Credits

* Developed by **Kimathi Elikplim Sedegah**
* Uses open-source libraries for Telegram and API integration
* ASCII diagrams designed for clarity in text-only environments

