from telegram import Update
from telegram.ext import ContextTypes
from config import ADMIN_ID
from db import add_user, get_all_users
from rashifol_data import rashifol

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    add_user(user_id)
    await update.message.reply_text("👋 স্বাগতম! বাংলা রাশিফল জানতে /rashifol রাশি নাম লিখুন।")

async def rashifol_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("🔮 উদাহরণ: /rashifol মেষ")
        return

    rashi = context.args[0].strip()
    message = rashifol.get(rashi)

    if message:
        await update.message.reply_text(f"🔮 আজকের রাশিফল ({rashi}):\n\n{message}")
    else:
        await update.message.reply_text("❌ রাশির নাম সঠিক নয়।")

async def broadcast(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("❌ আপনি এই কমান্ড ব্যবহার করতে পারবেন না।")
        return

    if not context.args:
        await update.message.reply_text("ব্যবহার করুন: /broadcast আপনার বার্তা")
        return

    msg = " ".join(context.args)
    users = get_all_users()
    sent = 0

    for uid in users:
        try:
            await context.bot.send_message(chat_id=uid, text=msg)
            sent += 1
        except:
            pass

    await update.message.reply_text(f"✅ {sent} জন ব্যবহারকারীর কাছে বার্তা পাঠানো হয়েছে।")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✳️ কমান্ড তালিকা:\n/start\n/rashifol [রাশি]\n/help\n/broadcast (শুধুমাত্র অ্যাডমিন)")
