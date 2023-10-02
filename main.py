import telebot
API_KEY = "6218242534:AAFL8ZNRM7CUTjNqUhASLOKIEXFohZ7GM0w"
bot = telebot.TeleBot(API_KEY, parse_mode=False)
@bot.message_handler(commands=["start"])
def start_message(msg):
    bot.reply_to(msg, "Please Join Our Telegram Channel for More Updates👇👇 \n @BC_Bot_projects \n Send /help to get help")

@bot.message_handler(commands=["help"])
def start_message(msg):
    bot.reply_to(msg, "This bot helps you to know your:  \n 🔰 Name \n 🔰 ID & \n 🔰 Username easily \n \n \n This bot is created with ☕ and ♥️ by @bek_i \n ✅ Join This Channel to get more bots and update 👇👇👇 \n @BC_bot_projects")  
@bot.message_handler(func= lambda message: True)
def start_message(msg):
    name = msg.from_user.first_name
    id = msg.from_user.id
    username = msg.from_user.username
    bot.reply_to(msg, "   Your Information \n  Id : "+str(id)+" \n Name : "+ name +"\n username = @" + username + "\n \n @BC_bot_projects")
    print("1")
print("running...")
bot.polling()
