from config import TG_BOT_API_KEY
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from utils import load_messages_for_bot


async def start(update: Update, context: ContextTypes):
    text = load_messages_for_bot("main")
    await update.message.reply_text(text)

app = ApplicationBuilder().token(TG_BOT_API_KEY).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()