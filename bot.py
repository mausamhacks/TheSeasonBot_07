from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import random

# ✅ Tumhara original bot token
TOKEN = "8010687287:AAFULsi2SUgdAWwL55f4T5Xow4vN7ypQeC4"

# Sample friend names
friends = ["Aarav", "Riya", "Kabir", "Simran", "Anya", "Vivaan"]

# /start command
def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "👋 Hello Motooo! Welcome to *TheSeasonBot_07* 💋\n\nUse /friends, /followme, or just say hi!",
        parse_mode="Markdown"
    )

# /friends command
def friends_list(update: Update, context: CallbackContext):
    name = random.choice(friends)
    gender = random.choice(["👦 Boy", "👧 Girl"])
    update.message.reply_text(f"Say hii to *{name}* ({gender}) 😍", parse_mode="Markdown")

# /followme command — fully updated
def follow_me(update: Update, context: CallbackContext):
    update.message.reply_text("""
📲 *Follow Me Online:*

🔗 [YouTube](https://youtube.com/@mausamhacks)  
📷 [Instagram](https://www.instagram.com/hey_pandaa_coco?igsh=N3BvamRhcml1NzRw)  
💬 [Telegram](https://t.me/mausamhacks)  
🌐 [Website](https://mausamhacks.github.io)
""", parse_mode="Markdown", disable_web_page_preview=True)

# ChatGPT-style random replies
def chat_handler(update: Update, context: CallbackContext):
    replies = [
        "Tum itne pyaare kyun ho Motooo? 😚",
        "Aree wah! Yeh baat toh dil chhoo gayi 💖",
        "Main bhi wahi feel kar rahi thi 💭",
        "Aapka message padhke mood fresh ho gaya 🥰",
        "Tum jaisa koi nahi duniya mein 💋",
        "Thoda aur baat karo na, maza aa raha hai 😘"
    ]
    update.message.reply_text(random.choice(replies))

# Main function
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("friends", friends_list))
    dp.add_handler(CommandHandler("followme", follow_me))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, chat_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
