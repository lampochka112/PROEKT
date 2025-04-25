from telegram.ext import ContextTypes
from telegram import Update
from utils.api_client import fetch_news

async def post_to_channel(context: ContextTypes.DEFAULT_TYPE):
    news = await fetch_news()  # Получаем данные из API
    await context.bot.send_message(
        chat_id=CHANNEL_ID,
        text=f"📢 Новость: {news['title']}\n\n{news['content']}"
    )

def setup_channel_handlers(app):
    app.job_queue.run_repeating(post_to_channel, interval=3600)  # Каждый час