from gitManual.lists.basics import basics

def start(update, context):

    update.message.reply_text(basics.START.value)
    update.message.reply_text(basics.GIT.value)

def quiskstart(update, context):
    
    update.message.reply_text(basics.QUICK.value)

def one(update, context):

    update.message.reply_text(basics.ONE.value)

def two(update, context):

    update.message.reply_text(basics.TWO.value)

def tree(update, context):

    update.message.reply_text(basics.TREE.value)

def four(update, context):

    update.message.reply_text(basics.FOUR.value)

def five(update, context):

    update.message.reply_text(basics.FIVE.value)

def six(update, context):

    update.message.reply_text(basics.SIX.value)