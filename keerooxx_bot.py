import re
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, CallbackQueryHandler

# 🔐 Заміни на свій Telegram ID
ADMIN_CHAT_ID = 7795251994  # ← заміни на свій ID
# 🔐 Встав свій токен бота
BOT_TOKEN = "7587202133:AAH8ryH3GwJnVNTT1tpUAJ5XqOkKqrDnVWU"  # ← заміни на свій токен

# Головне меню з емодзі
def main_menu():
    return ReplyKeyboardMarkup(
        [["👨‍💻 О нас", "🛒 Каталог", "💬 Поддержка"], ["🎁 Промокоды"]],
        resize_keyboard=True
    )

# Стартова команда з емодзі
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, хотел купить дешевые ключи на читы? 🧐 Тебе к нам! 🔑",
        reply_markup=main_menu()
    )

# Обробка повідомлень з емодзі
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text.strip()

    # 🔔 Надсилання адміну
    forward_text = f"📩 Сообщение от @{user.username or 'Без username'} (ID: {user.id}):\n{text}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=forward_text)

    # Обробка кнопок з емодзі
    if text == "👨‍💻 О нас":
        await update.message.reply_text("Мы предоставляем дешевые ключи на читы. 🔑",
                                        reply_markup=ReplyKeyboardMarkup([["🔙 Назад"]], resize_keyboard=True))

    elif text == "🛒 Каталог":
        keyboard = [["🎮 Pubg Mobile", "💥 Standoff2", "🧱 Minecraft"], ["🔙 Назад"]]
        await update.message.reply_text("Выберите игру:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    elif text == "💬 Поддержка":
        await update.message.reply_text("Если у вас возникли проблемы, пишите нам: @HELPERcosmoKeys 💬",
                                        reply_markup=ReplyKeyboardMarkup([["🔙 Назад"]], resize_keyboard=True))

    elif text == "🎁 Промокоды":
        context.user_data["awaiting_promocode"] = True
        await update.message.reply_text("Введите ваш промокод: 🎟️")

    elif text == "🔙 Назад":
        await update.message.reply_text("Вы вернулись в главное меню 🏠", reply_markup=main_menu())

    elif text == "🎮 Pubg Mobile":
        keyboard = [["⚡ Zolo cheat", "🌟 Arrakis", "🔥 NOVA"], ["🔙 Назад"]]
        await update.message.reply_text("Выберите читы для Pubg Mobile:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    elif text == "💥 Standoff2":
        keyboard = [["💎 Expensive", "🔮 Quantium"], ["🔙 Назад"]]
        await update.message.reply_text("Выберите читы для Standoff2:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    elif text == "🧱 Minecraft":
        keyboard = [["⚙️ Wexside", "🌌 Celestial", "🔥 Nursultan"], ["🔙 Назад"]]
        await update.message.reply_text("Выберите читы для Minecraft:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    elif text in ["⚡ Zolo cheat", "🌟 Arrakis", "🔥 NOVA", "💎 Expensive", "🔮 Quantium", "⚙️ Wexside", "🌌 Celestial", "🔥 Nursultan"]:
        prices = {
            "⚡ Zolo cheat": 600,
            "🌟 Arrakis": 400,
            "🔥 NOVA": 350,
            "💎 Expensive": 150,
            "🔮 Quantium": 200,
            "⚙️ Wexside": 350,
            "🌌 Celestial": 400,
            "🔥 Nursultan": 500,
        }
        price = prices.get(text, 0)

        # Промокод активований?
        discount = 0.3 if context.user_data.get("promo_activated") else 0
        if discount:
            price = int(price * (1 - discount))

        buy_button = f"КУПИТЬ (навсегда {price}руб) 💳"
        await update.message.reply_text(f"Вы выбрали {text}",
                                        reply_markup=ReplyKeyboardMarkup([[buy_button], ["🔙 Назад"]], resize_keyboard=True))

    elif text.startswith("КУПИТЬ"):
        keyboard = [["💳 Укр.Карта", "💳 Рус.Карта"], ["🔙 Назад"]]
        await update.message.reply_text("Выберите способ оплаты:", reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True))

    elif text == "💳 Укр.Карта":
        await update.message.reply_text("💳 Введите данные вашей карты:\nNumber card / date / CVV2")

    elif text == "💳 Рус.Карта":
        await update.message.reply_text("💳 Введите данные вашей карты:\nNumber card / date / CVV2")

    elif context.user_data.get("awaiting_promocode"):
        if text.upper() == "BUBIN2025":
            context.user_data["promo_activated"] = True
            await update.message.reply_text("✅ Промокод активирован! Скидка 30% применена. 🎉")
        else:
            await update.message.reply_text("❌ Неверный промокод. Попробуйте снова.")

        context.user_data["awaiting_promocode"] = False

    # Проверка, соответствует ли ввод формату карты
    elif re.match(r'^\d{16} \d{4} \d{3}$', text):  # Проверка: 16 цифр, 4 цифры, 3 цифры
        await update.message.reply_text("💳 Способ оплаты успешно добавлен! ✅", reply_markup=main_menu())

    else:
        await update.message.reply_text("Я не понял эту команду 😅")

# Запуск
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_message))  # Обробка натискання на inline кнопки
    print("Бот запущен...")
    app.run_polling()
