import os
import logging
from fastapi import FastAPI, Request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, AIORateLimiter

from algos.sorting import *
from algos.searching import *
from algos.recursion import *
from algos.structures import *

# Corrected environment variable usage
BOT_TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()
tg_app = Application.builder().token(BOT_TOKEN).rate_limiter(AIORateLimiter()).build()

async def respond(update: Update, text: str):
    await update.message.reply_text(text)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await respond(update, "Welcome to AlgoGraphBot. Try /bubble, /quick, /dfs, /factorial, etc.")

# Command handlers
tg_app.add_handler(CommandHandler("start", start))
tg_app.add_handler(CommandHandler("bubble", lambda u, c: respond(u, bubble_sort_visualization([5, 2, 8, 1]))))
tg_app.add_handler(CommandHandler("selection", lambda u, c: respond(u, selection_sort_visualization([4, 3, 1, 9]))))
tg_app.add_handler(CommandHandler("insertion", lambda u, c: respond(u, insertion_sort_visualization([9, 1, 5, 2]))))
tg_app.add_handler(CommandHandler("quick", lambda u, c: respond(u, quick_sort_visualization([5, 1, 3, 9]))))
tg_app.add_handler(CommandHandler("binary", lambda u, c: respond(u, binary_search_ascii())))
tg_app.add_handler(CommandHandler("linear", lambda u, c: respond(u, linear_search_ascii())))
tg_app.add_handler(CommandHandler("factorial", lambda u, c: respond(u, factorial_trace(4))))
tg_app.add_handler(CommandHandler("fibonacci", lambda u, c: respond(u, fibonacci_trace(5))))
tg_app.add_handler(CommandHandler("bfs", lambda u, c: respond(u, bfs_ascii())))
tg_app.add_handler(CommandHandler("dfs", lambda u, c: respond(u, dfs_ascii())))
tg_app.add_handler(CommandHandler("tree", lambda u, c: respond(u, tree_ascii())))
tg_app.add_handler(CommandHandler("graph", lambda u, c: respond(u, graph_ascii())))
tg_app.add_handler(CommandHandler("hashtable", lambda u, c: respond(u, hashtable_ascii())))
tg_app.add_handler(CommandHandler("stack", lambda u, c: respond(u, stack_ascii())))
tg_app.add_handler(CommandHandler("queue", lambda u, c: respond(u, queue_ascii())))

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    update = Update.de_json(data, tg_app.bot)
    await tg_app.process_update(update)
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    await tg_app.bot.set_webhook(WEBHOOK_URL)
