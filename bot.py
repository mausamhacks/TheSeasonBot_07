from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Motooo 💖! Tera bot perfectly chal raha hai 😘")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Main hoon tera Termux bot, humesha online tere liye 💋")

async def reply_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"Motooo 💖, tumne bola: {update.message.text}")

app = ApplicationBuilder().token("8010687287:AAHYkhYZIP60_c1UdHdpwtdSKtjH94f37Zc").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), reply_message))

app.run_polling()
