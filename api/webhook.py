import os
import logging
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, AIORateLimiter

from algos.descriptions import (
    sorting_descriptions,
    searching_descriptions,
    recursion_descriptions,
    structure_descriptions,
    traversal_descriptions
)

from algos.sorting import *
from algos.searching import *
from algos.recursion import *
from algos.structures import *
from algos.traversal import *

# Configuration
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# App setup
app = FastAPI()
tg_app = Application.builder().token(BOT_TOKEN).rate_limiter(AIORateLimiter()).build()

# Utility
async def respond(update: Update, text: str):
    if update.message:
        await update.message.reply_text(text)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await respond(update, """Welcome to AlgoGraphBot!

I can walk you through popular algorithms with step-by-step explanations.

Try one of these commands to begin:

Sorting:
  /bubble     - Bubble Sort
  /insertion  - Insertion Sort
  /selection  - Selection Sort
  /quick      - Quick Sort

Searching:
  /linear     - Linear Search
  /binary     - Binary Search

Recursion:
  /factorial  - Factorial Trace
  /fibonacci  - Fibonacci Trace

Data Structures:
  /stack      - Stack
  /queue      - Queue
  /tree       - Tree
  /graph      - Graph
  /hashtable  - Hash Table

Traversal:
  /bfs        - Breadth-First Search
  /dfs        - Depth-First Search
""")

# Command Handlers
tg_app.add_handler(CommandHandler("start", start))

# Sorting
tg_app.add_handler(CommandHandler("bubble", lambda u, c: respond(
    u, f"{sorting_descriptions['bubble']}\n\n{bubble_sort_steps([5, 2, 8, 1])}")))

tg_app.add_handler(CommandHandler("insertion", lambda u, c: respond(
    u, f"{sorting_descriptions['insertion']}\n\n{insertion_sort_steps([9, 1, 5, 2])}")))

tg_app.add_handler(CommandHandler("selection", lambda u, c: respond(
    u, f"{sorting_descriptions['selection']}\n\n{selection_sort_steps([4, 3, 1, 9])}")))

tg_app.add_handler(CommandHandler("quick", lambda u, c: respond(
    u, f"{sorting_descriptions['quick']}\n\n{quick_sort_steps([5, 1, 3, 9])}")))

# Searching
tg_app.add_handler(CommandHandler("linear", lambda u, c: respond(
    u, f"{searching_descriptions['linear']}\n\n{linear_search_steps([3, 1, 4, 2], 4)}")))

tg_app.add_handler(CommandHandler("binary", lambda u, c: respond(
    u, f"{searching_descriptions['binary']}\n\n{binary_search_steps([1, 3, 5, 7, 9], 5)}")))

# Recursion
tg_app.add_handler(CommandHandler("factorial", lambda u, c: respond(
    u, f"{recursion_descriptions['factorial']}\n\n{factorial_steps(4)}")))

tg_app.add_handler(CommandHandler("fibonacci", lambda u, c: respond(
    u, f"{recursion_descriptions['fibonacci']}\n\n{fibonacci_steps(5)}")))

# Data Structures
tg_app.add_handler(CommandHandler("stack", lambda u, c: respond(
    u, f"{structure_descriptions['stack']}\n\n{stack_steps()}")))

tg_app.add_handler(CommandHandler("queue", lambda u, c: respond(
    u, f"{structure_descriptions['queue']}\n\n{queue_steps()}")))

tg_app.add_handler(CommandHandler("tree", lambda u, c: respond(
    u, f"{structure_descriptions['tree']}\n\n{tree_steps()}")))

tg_app.add_handler(CommandHandler("graph", lambda u, c: respond(
    u, f"{structure_descriptions['graph']}\n\n{graph_steps()}")))

tg_app.add_handler(CommandHandler("hashtable", lambda u, c: respond(
    u, f"{structure_descriptions['hashtable']}\n\n{hashtable_steps()}")))

# Traversal
tg_app.add_handler(CommandHandler("bfs", lambda u, c: respond(
    u, f"{traversal_descriptions['bfs']}\n\n{bfs_steps()}")))

tg_app.add_handler(CommandHandler("dfs", lambda u, c: respond(
    u, f"{traversal_descriptions['dfs']}\n\n{dfs_steps()}")))

# Webhook endpoint
@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, tg_app.bot)
    await tg_app.process_update(update)
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    await tg_app.initialize()
    await tg_app.bot.set_webhook(WEBHOOK_URL)
    await tg_app.start()

@app.get("/")
async def root():
    return {"status": "AlgoGraphBot is alive!"}


@app.on_event("shutdown")
async def on_shutdown():
    await tg_app.stop()
    await tg_app.shutdown()
