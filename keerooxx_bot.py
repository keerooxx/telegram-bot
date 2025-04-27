from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# Стартова команда
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["О нас", "Каталог", "Поддержка"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Привет, хотел купить дешевые ключи на читы? Тебе к нам!", reply_markup=reply_markup)

# Обробка всіх повідомлень
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    if text == "О нас":
        keyboard = [["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Мы предоставляем дешевые ключи на читы.", reply_markup=reply_markup)

    elif text == "Каталог":
        keyboard = [["Pubg Mobile", "Standoff2", "Minecraft"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите игру:", reply_markup=reply_markup)

    elif text == "Поддержка":
        keyboard = [["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Если у вас возникли проблемы, пишите нам в поддержку: @HELPERcosmoKeys", reply_markup=reply_markup)

    elif text == "Pubg Mobile":
        keyboard = [["Zolo cheat", "Arrakis", "NOVA"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите читы для Pubg Mobile:", reply_markup=reply_markup)

    elif text == "Standoff2":
        keyboard = [["Expensive", "Quantium"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите читы для Standoff2:", reply_markup=reply_markup)

    elif text == "Minecraft":
        keyboard = [["Wexside", "Celestial", "Nursultan"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите читы для Minecraft:", reply_markup=reply_markup)

    # Обработка читов
    elif text == "Zolo cheat":
        keyboard = [["КУПИТЬ (навсегда 300руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Zolo cheat для Pubg Mobile", reply_markup=reply_markup)

    elif text == "Arrakis":
        keyboard = [["КУПИТЬ (навсегда 250руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Arrakis для Pubg Mobile", reply_markup=reply_markup)

    elif text == "NOVA":
        keyboard = [["КУПИТЬ (навсегда 200руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали NOVA для Pubg Mobile", reply_markup=reply_markup)

    elif text == "Expensive":
        keyboard = [["КУПИТЬ (навсегда 150руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Expensive для Standoff2", reply_markup=reply_markup)

    elif text == "Quantium":
        keyboard = [["КУПИТЬ (навсегда 170руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Quantium для Standoff2", reply_markup=reply_markup)

    elif text == "Wexside":
        keyboard = [["КУПИТЬ (навсегда 199руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Wexside для Minecraft", reply_markup=reply_markup)

    elif text == "Celestial":
        keyboard = [["КУПИТЬ (навсегда 230руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Celestial для Minecraft", reply_markup=reply_markup)

    elif text == "Nursultan":
        keyboard = [["КУПИТЬ (навсегда 249руб)"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы выбрали Nursultan для Minecraft", reply_markup=reply_markup)

    # Обработка покупки — универсально
    elif text.startswith("КУПИТЬ"):
        keyboard = [["Укр.Карта", "Рус.Карта"], ["Назад"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Выберите способ оплаты:", reply_markup=reply_markup)

    # Обработка способов оплаты
    elif text == "Укр.Карта":
        await update.message.reply_text("💳 Оплата на украинскую карту: 4149 **** **** ****\nПосле оплаты — напишите в поддержку.")

    elif text == "Рус.Карта":
        await update.message.reply_text("💳 Оплата на российскую карту: 2202 **** **** ****\nПосле оплаты — напишите в поддержку.")

    # Назад в главное меню
    elif text == "Назад":
        keyboard = [["О нас", "Каталог", "Поддержка"]]
        reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
        await update.message.reply_text("Вы вернулись в главное меню", reply_markup=reply_markup)

    else:
        await update.message.reply_text("Я не понял эту команду 😅")

# Запуск бота
if __name__ == "__main__":
    app = ApplicationBuilder().token("7587202133:AAH8ryH3GwJnVNTT1tpUAJ5XqOkKqrDnVWU").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()
