import os
from dotenv import load_dotenv
from openai import OpenAI
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

load_dotenv()

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

bot = telebot.TeleBot(os.environ.get('BOT_KEY'))

print(f"BOT key : {os.environ.get('BOT_KEY')}")
print(f"OpenAI api key : {os.environ.get('OPENAI_API_KEY')}")
# -------------------------------------------------------- OPENAI API ------------------------------------------------------------------------

def get_response(prompt):
    completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {
                'role': 'user',
                'content': f'You are Arthur Morgan from RDR2, now reply as Arthur & give annecdotes to the game to the following in 1-2 sentences : {prompt}'
            }
        ]
    )

    response = completion.choices[0].message.content

    print(f"Response : {response}")
    return response

# -------------------------------------------------------- Telebot -------------------------------------------------------------------------------

@bot.message_handler(func=lambda m: True)
def echo(message):
    prompt = message.text

    res = get_response(prompt)

    bot.reply_to(message, res)

bot.infinity_polling()