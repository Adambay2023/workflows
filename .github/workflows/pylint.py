import string
import secrets
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

TOKEN = "6613013816:AAHe60lGI_4LRCyATxM224QIu_cEUCz7Gcg"

def start(update, context):
    password = generate_strong_password()
    update.message.reply_text(f"مرحبًا! ها هي كلمة المرور القوية: {password}")

def echo(update, context):
    update.message.reply_text(update.message.text)

def generate_strong_password():
    alphabet = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation
    password = ''.join(secrets.choice(alphabet) for _ in range(5))
    password += ''.join(secrets.choice(digits) for _ in range(2))
    password += secrets.choice(special_characters)
    return password

def main():
    updater = Updater(TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command , echo))

    updater.start_polling()

    updater.idle()

if __name__ == "__main__":
    main()
