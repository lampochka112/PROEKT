from telegram.ext import Application, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN
from handlers.group import setup_group_handlers
from handlers.channel import setup_channel_handlers
from handlers.private import setup_private_handlers
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update, context):
    await update.message.reply_text("Привет! Я многофункциональный бот.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    setup_group_handlers(app)
    setup_channel_handlers(app)
    setup_private_handlers(app)

    app.run_polling()

if __name__ == "__main__":
    main()