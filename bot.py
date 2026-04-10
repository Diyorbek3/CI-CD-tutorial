import telebot

TOKEN = '8672475093:AAGPZ6ntcEqnX8slyV0nSJ2pVQoYZKU4Rvk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Matnni o'zgartiramiz
    text = "Assalomu alaykum, Diyorbek! 🔥\n\nBu xabar GitHub Actions orqali avtomat keldi. Tizim holati: ONLINE ✅"
    bot.reply_to(message, text)

print("Bot yoqildi...")
bot.infinity_polling()