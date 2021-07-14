from telegram.ext import Updater, CommandHandler
from credentials import credential
from gitManual.functions.basics import start, quiskstart, one, two, tree, four, five

if __name__ == '__main__':

    updater = Updater(token=credential, use_context=True)

    dp = updater.dispatcher

# Basics

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('quickstart', quiskstart))
    dp.add_handler(CommandHandler('stepOne', one))
    dp.add_handler(CommandHandler('stepTwo', two))
    dp.add_handler(CommandHandler('stepTree', tree))
    dp.add_handler(CommandHandler('stepFour', four))
    dp.add_handler(CommandHandler('stepFive', five))

#Start

    updater.start_polling()

    print('starting bot')

    updater.idle()

    print("Finished")