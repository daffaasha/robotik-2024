import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import RPi.GPIO as GPIO

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

# Token dari BotFather
TOKEN = 'YOUR_BOT_TOKEN'

def start(update, context):
    update.message.reply_text('Hai, saya Japran, apa yang bisa saya bantu?')

def turn_on(update, context):
    GPIO.output(18, GPIO.HIGH)
    update.message.reply_text('LED Nyala')

def turn_off(update, context):
    GPIO.output(18, GPIO.LOW)
    update.message.reply_text('LED Tewas')

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("on", turn_on))
    dp.add_handler(CommandHandler("off", turn_off))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
