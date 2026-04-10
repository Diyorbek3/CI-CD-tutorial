import telebot

TOKEN = '8672475093:AAGPZ6ntcEqnX8slyV0nSJ2pVQoYZKU4Rvk'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalom! Men eski tizimda ishlayapman.")

print("Bot yoqildi...")
bot.infinity_polling()