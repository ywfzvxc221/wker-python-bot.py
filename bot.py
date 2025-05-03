from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# دالة الرد عند بدء المحادثة
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا هنا للرد على رسائلك.')

# دالة الرد على أي رسالة نصية
def reply_message(update: Update, context: CallbackContext) -> None:
    text_received = update.message.text
    update.message.reply_text(f'أنت قلت: {text_received}')

def main() -> None:
    # استبدال التوكن
    updater = Updater("7609490900:AAGdsG7LTImVgdSEfM3Y62Qx7dmWljzkUYk")

    # الوصول إلى الموزع
    dispatcher = updater.dispatcher

    # إضافة معالجات للأوامر والرسائل
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_message))

    # بدء البوت
    updater.start_polling()

    # الانتظار حتى يتم إيقاف البوت
    updater.idle()

if __name__ == '__main__':
    main()
