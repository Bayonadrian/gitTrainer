from telegram.ext import Updater, CommandHandler
from credentials import credential
from gitManual.functions.basics import start, quiskstart, one, two, tree

if __name__ == '__main__':

    updater = Updater(token=credential, use_context=True)

    dp = updater.dispatcher

# Basics

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('quickstart', quiskstart))
    dp.add_handler(CommandHandler('stepOne', one))
    dp.add_handler(CommandHandler('stepTwo', two))
    dp.add_handler(CommandHandler('stepTree', tree))

#Start

    updater.start_polling()

    print('starting bot')

    updater.idle()

    print("Finished")