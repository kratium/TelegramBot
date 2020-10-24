import logging

from telegram.ext import Updater, CommandHandler

logging.basicConfig(
    level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')



updater = Updater(
    token='1156998329:AAHGaJj867D9qdfQixKrhEWqdepmshWS0_k'
    )
dispatcher = updater.dispatcher

def start(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Hello World!",
    )

def jokes(upd, ctx):
    ctx.bot.send_message(
        chat_id=upd.effective_chat.id,
        text="Анекдот: в детдоме сиротам раздали сок Моя семья!",
    )

start_handler = CommandHandler(
    'start', start
    )

jokes_handler = CommandHandler(
    'jokes', jokes
    )

dispatcher.add_handler(start_handler)
dispatcher.add_handler(jokes_handler)

updater.start_polling()