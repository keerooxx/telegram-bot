import re
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters, CallbackQueryHandler

ADMIN_CHAT_ID = 7795251994
BOT_TOKEN = "7587202133:AAH8ryH3GwJnVNTT1tpUAJ5XqOkKqrDnVWU"

# Константы для кнопок меню
MENU_ABOUT = "👨‍💻 О нас"
MENU_CATALOG = "🛒 Каталог"
MENU_SUPPORT = "💬 Поддержка"
MENU_PROMOS = "🎁 Промокоды"
MENU_BACK = "🔙 Назад"

# Константы для игр
GAME_PUBG = "🎮 Pubg Mobile"
GAME_STANDOFF = "💥 Standoff2"
GAME_MINECRAFT = "🧱 Minecraft"

# Словарь цен на читы
PRICES = {
    "⚡ Zolo cheat": 600,
    "🌟 Arrakis": 400,
    "🔥 NOVA": 350,
    "💎 Expensive": 150,
    "🔮 Quantium": 200,
    "⚙️ Wexside": 350,
    "🌌 Celestial": 400,
    "🔥 Nursultan": 500,
}

def main_menu():
    return ReplyKeyboardMarkup(
        [[MENU_ABOUT, MENU_CATALOG, MENU_SUPPORT], [MENU_PROMOS]],
        resize_keyboard=True
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, хотел купить дешевые ключи на читы? 🧐 Тебе к нам! 🔑",
        reply_markup=main_menu()
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text.strip()

    # Отправка сообщения администратору
    forward_text = f"📩 Сообщение от @{user.username or 'Без username'} (ID: {user.id}):\n{text}"
    await context.bot.send_message(chat_id=ADMIN_CHAT_ID, text=forward_text)

    # Обработка меню "О нас"
    if text == MENU_ABOUT:
        await update.message.reply_text(
            "Мы предоставляем дешевые ключи на читы. 🔑",
            reply_markup=ReplyKeyboardMarkup([[MENU_BACK]], resize_keyboard=True)
        )

    # Обработка меню "Каталог"
    elif text == MENU_CATALOG:
        keyboard = [[GAME_PUBG, GAME_STANDOFF, GAME_MINECRAFT], [MENU_BACK]]
        await update.message.reply_text(
            "Выберите игру:", 
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # Обработка меню "Поддержка"
    elif text == MENU_SUPPORT:
        await update.message.reply_text(
            "Если у вас возникли проблемы, пишите нам: @HELPERcosmoKeys 💬",
            reply_markup=ReplyKeyboardMarkup([[MENU_BACK]], resize_keyboard=True)
        )

    # Обработка меню "Промокоды"
    elif text == MENU_PROMOS:
        context.user_data["awaiting_promocode"] = True
        await update.message.reply_text("Введите ваш промокод: 🎟️")

    # Обработка кнопки "Назад"
    elif text == MENU_BACK:
        await update.message.reply_text("Вы вернулись в главное меню 🏠", reply_markup=main_menu())

    # Обработка выбора игры PUBG
    elif text == GAME_PUBG:
        keyboard = [["⚡ Zolo cheat", "🌟 Arrakis", "🔥 NOVA"], [MENU_BACK]]
        await update.message.reply_text(
            "Выберите читы для Pubg Mobile:", 
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # Обработка выбора игры Standoff2
    elif text == GAME_STANDOFF:
        keyboard = [["💎 Expensive", "🔮 Quantium"], [MENU_BACK]]
        await update.message.reply_text(
            "Выберите читы для Standoff2:", 
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # Обработка выбора игры Minecraft
    elif text == GAME_MINECRAFT:
        keyboard = [["⚙️ Wexside", "🌌 Celestial", "🔥 Nursultan"], [MENU_BACK]]
        await update.message.reply_text(
            "Выберите читы для Minecraft:", 
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # Обработка выбора чита
    elif text in PRICES:
        price = PRICES[text]
        
        # Применение скидки по промокоду
        discount = 0.3 if context.user_data.get("promo_activated") else 0
        if discount:
            price = int(price * (1 - discount))

        buy_button = f"КУПИТЬ (навсегда {price}руб) 💳"
        await update.message.reply_text(
            f"Вы выбрали {text}",
            reply_markup=ReplyKeyboardMarkup([[buy_button], [MENU_BACK]], resize_keyboard=True)
        )

    # Обработка кнопки покупки
    elif text.startswith("КУПИТЬ"):
        keyboard = [["💳 Укр.Карта", "💳 Рус.Карта"], [MENU_BACK]]
        await update.message.reply_text(
            "Выберите способ оплаты:", 
            reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        )

    # Обработка выбора способа оплаты
    elif text in ["💳 Укр.Карта", "💳 Рус.Карта"]:
        await update.message.reply_text("💳 Введите данные вашей карты:\nNumber card / date / CVV2")

    # Обработка ввода промокода
    elif context.user_data.get("awaiting_promocode"):
        if text.upper() == "BUBIN2025":
            context.user_data["promo_activated"] = True
            await update.message.reply_text("✅ Промокод активирован! Скидка 30% применена. 🎉")
        else:
            await update.message.reply_text("❌ Неверный промокод. Попробуйте снова.")

        context.user_data["awaiting_promocode"] = False
        await update.message.reply_text("Вернуться в меню?", reply_markup=main_menu())

    # Проверка формата карты
    elif re.match(r'^\d{16} \d{4} \d{3}$', text):
        await update.message.reply_text("💳 Способ оплаты успешно добавлен! ✅", reply_markup=main_menu())

    # Обработка неизвестных команд
    else:
        await update.message.reply_text("Я не понял эту команду 😅", reply_markup=main_menu())

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CallbackQueryHandler(handle_message))
    print("Бот запущен...")
    app.run_polling()
