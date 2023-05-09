from telegram import Bot
from telegram.ext import CommandHandler, CallbackQueryHandler, CallbackContext, Updater

bot = Bot(token='5701805679:AAGjauOjevEn4tGDZAsURJm7DzsNEGshn0A')

def kirim_pesan(update, context):
    chat_id = update.effective_chat.id
    context.bot.send_message(chat_id=chat_id, text='Silakan bergabung dengan channel kami untuk menggunakan bot ini')

def periksa_channel(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    member = context.bot.get_chat_member('@pekobkun', user_id)
    if member.status == 'left':
        kirim_pesan(update, context)

def cyclic_check(context: CallbackContext):
    members = context.bot.get_chat_members_count('@pekobkun')
    context.job_queue.run_repeating(cyclic_check, interval=300, first=0)
    if members <= 1:
        kirim_pesan(update, context)

start_handler = CommandHandler('start', periksa_channel)
cyclic_handler = CallbackQueryHandler(cyclic_check)

updater = Updater(token='5701805679:AAGjauOjevEn4tGDZAsURJm7DzsNEGshn0A', use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(start_handler)
dispatcher.add_handler(cyclic_handler)

updater.start_polling()
