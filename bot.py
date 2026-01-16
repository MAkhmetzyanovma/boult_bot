from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    keyboard = [
        [InlineKeyboardButton("👨‍🔧 Написать специалисту", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("🛒 Заказ запчастей", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("🚗 Заказ ноускатов", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("🚚 Заказ машинокомплектов", url=f"https://t.me/{USERNAME_SPECIALIST}")],
        [InlineKeyboardButton("📘 Получить подробную информацию по ноускатам", callback_data="nous_info")],
        [InlineKeyboardButton("📝 Как производится заказ?", callback_data="how_order")],
        [InlineKeyboardButton("📍 Как нас найти?", callback_data="contacts")]
    ]

    await update.message.reply_text(
        text="Выберите интересующий вас вариант 👇",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --- Контакты ---
    if query.data == "contacts":
        await query.message.reply_text(
            "📍 *Контакты Boult Auto*\n\n"
            "📞 Телефоны: +7(993) 424-00-68  +7(950) 314-00-68\n"
            "📩 Telegram: @boultauto1\n"
            "🌐 Сайт: https://boult-auto.ru/\n"
            "📦 Работаем по всей России",
            parse_mode="Markdown"
        )

    # --- Как производится заказ ---
    elif query.data == "how_order":
        await query.message.reply_text(
"""📝 *Как производится заказ*
1. Выбор запчастей
2. Оплата агрегата
3. Отгрузка и транспортировка
4. Стоимость доставки кузовных частей
5. Сроки и логистика
6. Индивидуальные контейнеры
""",
            parse_mode="Markdown"
        )

    # --- Подробная информация по ноускатам ---
    elif query.data == "nous_info":
        keyboard = [
            [InlineKeyboardButton("Audi", callback_data="nous_audi")],
            [InlineKeyboardButton("BMW", callback_data="nous_bmw")],
            [InlineKeyboardButton("Mercedes", callback_data="nous_mercedes")],
            [InlineKeyboardButton("Volkswagen", callback_data="nous_volkswagen")]
        ]

        await query.message.reply_text(
            "🚗 Ноускат на какую модель вас интересует?",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )

    # --- Модели ---
    elif query.data == "nous_audi":
        await query.message.reply_text(
            "Информация по данной модели:\nhttps://машинокомплект.рф/nosecut"
        )

    elif query.data == "nous_bmw":
        await query.message.reply_text(
            "Информация по данной модели:\nhttps://машинокомплект.рф/nosecut"
        )

    elif query.data == "nous_mercedes":
        await query.message.reply_text(
            "Информация по данной модели:\nhttps://машинокомплект.рф/nosecut"
        )

    elif query.data == "nous_volkswagen":
        await query.message.reply_text(
            "Информация по данной модели:\nhttps://машинокомплект.рф/nosecut"
        )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(buttons))

app.run_polling()
