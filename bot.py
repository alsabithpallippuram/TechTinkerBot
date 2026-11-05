import os
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from groq import Groq

# നിങ്ങളുടെ ഗ്രോഖ് API കീ ഇവിടെ നൽകിയിരിക്കുന്നു
client = Groq(api_key="Gsk_eC3aRxCEd8z96OjpS7IhWGdyb3FYlWhqZwPIeAmKwbubIjHzI8TW")

# /start കമാൻഡ് കൊടുത്താൽ വരുന്ന വെൽക്കം മെസ്സേജ്
async def start(command_update: Update, context: ContextTypes.DEFAULT_TYPE):
    await command_update.message.reply_text(
        "Hello! I am your TechTinker AI Assistant powered by Groq. 🤖⚡\n"
        "Ask me anything about electronics, Arduino, sensors, or circuit debugging!"
    )

# യൂസർ അയക്കുന്ന മെസ്സേജുകൾക്ക് AI വഴി മറുപടി നൽകാൻ
async def handle_message(message_update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = message_update.message.text
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are TechTinker AI, a friendly and expert assistant specialized in electronics, robotics, Arduino, microcontrollers, and DIY hardware projects."
                },
                {
                    "role": "user",
                    "content": user_message,
                }
            ],
            model="llama3-8b-8192",
        )
        bot_reply = chat_completion.choices[0].message.content
    except Exception as e:
        bot_reply = "Sorry, I encountered an error processing your electronics query. Please try again!"

    await message_update.message.reply_text(bot_reply)

if __name__ == '__main__':
    # ബോട്ട്ഫാദറിൽ നിന്ന് കിട്ടിയ നിങ്ങളുടെ ടെലിഗ്രാം ടോക്കൺ
    application = ApplicationBuilder().token("9069701290:AAGnzxtMh8jDvnY3hpyfoZCQ9DdegtDN_Y").build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("TechTinker AI Bot is running smoothly...")
    application.run_polling()
