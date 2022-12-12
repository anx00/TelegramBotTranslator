import requests
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

# Replace with your own Telegram API key
TELEGRAM_API_KEY = ""

# Replace with your own DeepL API key
DEEPL_API_KEY = ""

# Set the language pair for translation (Spanish-Turkish in this example)
LANGUAGE_PAIR = "tr"

# URL for the DeepL API
DEEPL_API_URL = "https://api-free.deepl.com/v2/translate"

# Function to translate a message using the DeepL API
def translate_message(message, language_pair):
    data = {
        "auth_key": DEEPL_API_KEY,
        "text": message,
        "target_lang": language_pair,
        "source_lang": 'ES'
    }

    response = requests.post(DEEPL_API_URL, data=data)
    response_json = response.json()
    print(response_json)
    return response_json["translations"][0]["text"]


# Function to handle incoming messages
def handle_message(update, context):

    chat = update.message.chat
    print(chat)

    if context.user_data.get("translating", False):
		message = update.message.text
		translated_message = translate_message(message, LANGUAGE_PAIR)
		translated_message_en = translate_message(message, 'en')
		if LANGUAGE_PAIR == 'tr':
			context.bot.send_message(chat_id=update.message.chat_id,
									 text='🇹🇷' + ": " + translated_message + "\n🇬🇧: " + translated_message_en)
		elif LANGUAGE_PAIR == 'es':
			context.bot.send_message(chat_id=update.message.chat_id,
									 text='🇪🇸' + ": " + translated_message + "\n🇬🇧: " + translated_message_en)
		else:
			context.bot.send_message(chat_id=update.message.chat_id,
									 text=LANGUAGE_PAIR + ": " + translated_message + "\n🇬🇧: " + translated_message_en)


def start_translation(update, context):
    # Set a flag to indicate that the bot is now translating
    context.user_data["translating"] = True
    context.bot.send_message(chat_id=update.message.chat_id, text="Starting translation!")


def stop_translation(update, context):
    # Set the flag to indicate that the bot is no longer translating
    context.user_data["translating"] = False
    context.bot.send_message(chat_id=update.message.chat_id, text="Stopping translation!")


# Function to handle the /changelang command
def handle_changelang(update, context):
    # Get the new language code from the user's message
    new_lang_code = update.message.text.split()[1]
    # Update the global language pair variable
    global LANGUAGE_PAIR
    LANGUAGE_PAIR = new_lang_code
    # Send a confirmation message to the user
    context.bot.send_message(chat_id=update.message.chat_id, text="Language pair updated to: " + LANGUAGE_PAIR)

# Create the Updater and pass it your API key.
updater = Updater(TELEGRAM_API_KEY, use_context=True)

# Get the dispatcher to register handlers
dp = updater.dispatcher

# Add a handler to handle the /start command
dp.add_handler(CommandHandler("start", start_translation))

# Add a handler to handle the /stop command
dp.add_handler(CommandHandler("stop", stop_translation))

# Add a handler to handle the /changelang command
dp.add_handler(CommandHandler("changelang", handle_changelang))

# Add a handler to handle messages
dp.add_handler(MessageHandler(Filters.text,handle_message))

# Start the Bot
updater.start_polling()

# Run the bot until you press Ctrl-C or the process receives SIGINT,
# SIGTERM or SIGABRT. This should be used most of the time, since
# start_polling() is non-blocking and will stop the bot gracefully.
updater.idle()