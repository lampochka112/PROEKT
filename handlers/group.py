from telegram.ext import MessageHandler, filters
from telegram import Update
from telegram.ext import ContextTypes
import re

BAD_WORDS = ["мат1", "мат2"]  # Запрещенные слова

async def filter_bad_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if any(word in text for word in BAD_WORDS):
        await update.message.delete()
        await update.message.reply_text("⚠️ Не используйте запрещенные слова!")

async def game_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Игра начата! Угадайте число от 1 до 10.")

def setup_group_handlers(app):
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, filter_bad_words))
    app.add_handler(CommandHandler("game", game_start))