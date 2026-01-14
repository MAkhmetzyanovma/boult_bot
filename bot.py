import telebot
import os

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

from dotenv import load_dotenv
load_dotenv()  # Загружает .env файл
TOKEN = os.getenv('BOT_TOKEN')
USERNAME_SPECIALIST = "BoultAuto"

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("👨‍🔧 Написать специалисту", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("🛒 Заказ запчастей", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("🚗 Заказ ноускатов", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("🚚 Заказ машинокомплектов", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("📍 Как нас найти?", callback_data="contacts")]
    ]

    await update.message.reply_text(
        text="Выберите интересующий вас вариант 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

# Обработка кнопки "Как нас найти?"
async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "contacts":
        contacts_text = (
            "📍 *Контакты Boult Auto*\n\n"
            "📞 Телефоны: +7(993) 424-00-68  +7(950) 314-00-68\n"
            "📩 Telegram: @boultauto1\n"
            "🌐 Сайт: https://boult-auto.ru/\n"
            "📦 Работаем по всей России"
        )

        await query.message.reply_text(
            contacts_text,
            parse_mode="Markdown"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
