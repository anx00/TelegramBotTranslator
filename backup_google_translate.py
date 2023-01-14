import requests


def google_translate(text, dest_lang):
    r_url = f"https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl={dest_lang}&q={text}"
    try:
        resp = requests.get(r_url).json()[0]
        translation = resp[0]
        origin_text = text
        origin_lang = "es"
        dest_lang_f = dest_lang
        tr_dict = {"status": "success", "engine": "Google Translate", "translation": translation,
                   "dest_lang": dest_lang_f, "orgin_text": origin_text, "origin_lang": origin_lang}
        return tr_dict
    except Exception as e:
        return {"status": "failed", "error": e}

# Function to translate a message using the py_trans library
def translate_message_backup(message, language_pair):
    try:
        # Translate the message
        translated_message = google_translate(message,language_pair)['translation']
        print(translated_message)
    except Exception as e:
        # Handle any errors that may occur
        print("Error occurred while trying to translate message using py_trans")
        print(e)
        return None
    return translated_message