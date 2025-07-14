import os
import logging
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, AIORateLimiter

from algos.sorting import *
from algos.searching import *
from algos.recursion import *
from algos.structures import *
from algos.traversal import *  

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
tg_app = Application.builder().token(BOT_TOKEN).rate_limiter(AIORateLimiter()).build()

async def respond(update: Update, text: str):
    if update.message:
        await update.message.reply_text(text)

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

# Command handlers
tg_app.add_handler(CommandHandler("start", start))
tg_app.add_handler(CommandHandler("bubble", lambda u, c: respond(u, bubble_sort_steps([5, 2, 8, 1]))))
tg_app.add_handler(CommandHandler("selection", lambda u, c: respond(u, selection_sort_steps([4, 3, 1, 9]))))
tg_app.add_handler(CommandHandler("insertion", lambda u, c: respond(u, insertion_sort_steps([9, 1, 5, 2]))))
tg_app.add_handler(CommandHandler("quick", lambda u, c: respond(u, quick_sort_steps([5, 1, 3, 9]))))

tg_app.add_handler(CommandHandler("binary", lambda u, c: respond(u, binary_search_steps([1, 3, 5, 7, 9], 5))))
tg_app.add_handler(CommandHandler("linear", lambda u, c: respond(u, linear_search_steps([3, 1, 4, 2], 4))))

tg_app.add_handler(CommandHandler("factorial", lambda u, c: respond(u, factorial_steps(4))))  
tg_app.add_handler(CommandHandler("fibonacci", lambda u, c: respond(u, fibonacci_steps(5))))  

tg_app.add_handler(CommandHandler("bfs", lambda u, c: respond(u, bfs_steps())))
tg_app.add_handler(CommandHandler("dfs", lambda u, c: respond(u, dfs_steps())))
tg_app.add_handler(CommandHandler("tree", lambda u, c: respond(u, tree_steps())))
tg_app.add_handler(CommandHandler("graph", lambda u, c: respond(u, graph_steps())))

tg_app.add_handler(CommandHandler("hashtable", lambda u, c: respond(u, hashtable_steps())))
tg_app.add_handler(CommandHandler("stack", lambda u, c: respond(u, stack_steps())))
tg_app.add_handler(CommandHandler("queue", lambda u, c: respond(u, queue_steps())))

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

@app.on_event("shutdown")
async def on_shutdown():
    await tg_app.stop()
    await tg_app.shutdown()
