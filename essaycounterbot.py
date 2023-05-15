import configparser
import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, filters, MessageHandler,ConversationHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Lets count!')


def count_par (essay):
    essay = essay.split('\n')
    count = 0
    print(essay)
    for i in essay:
        if i.strip() != '':
            count += 1
    return(count)


def count_words(pars):
    symbols = [',', '.', '!', '?', '-', ':', ';', '"']
    counter = 0
    pars = pars.split('\n')
    for i in range(len(pars)):
        words = pars[i].split()
        for j in words:
            if j not in symbols:
                counter+=1
    return(counter)


async def get_essay(update: Update, context: ContextTypes.DEFAULT_TYPE):
    essay = update.message.text
    pars = count_par(essay)
    words = count_words(essay)
    await update.message.reply_html(f'<b>Number of paragraphs: {pars}</b>\n<b>Number of words: {words}</b>')



if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('config.ini')
    application = ApplicationBuilder().token(config['bot']['token']).build()
    start_handler = CommandHandler('start', start)
    essay_handler = MessageHandler(filters.TEXT, get_essay)

    application.add_handler(start_handler)
    application.add_handler(essay_handler)
    application.run_polling()