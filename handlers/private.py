from telegram.ext import ConversationHandler, CommandHandler, MessageHandler
from telegram import ReplyKeyboardMarkup

STATE_PHOTO = 1

async def start_dialog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [["Фото", "Текст"], ["Отмена"]]
    markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True)
    await update.message.reply_text("Выберите действие:", reply_markup=markup)
    return STATE_PHOTO

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(photo="https://example.com/image.jpg")
    return ConversationHandler.END

def setup_private_handlers(app):
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("dialog", start_dialog)],
        states={
            STATE_PHOTO: [
                MessageHandler(filters.TEXT & ~filters.COMMAND, handle_photo)
            ],
        },
        fallbacks=[]
    )
    app.add_handler(conv_handler)