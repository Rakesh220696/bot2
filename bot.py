from telegram.ext import ApplicationBuilder, CommandHandler
from handlers import start, rashifol_command, broadcast, help_command
from config import BOT_TOKEN
from db import init_db

def main():
    init_db()
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("rashifol", rashifol_command))
    app.add_handler(CommandHandler("broadcast", broadcast))
    app.add_handler(CommandHandler("help", help_command))

    print("🤖 Bengali Rashifol Bot চলছে...")
    app.run_polling()

if __name__ == '__main__':
    main()
