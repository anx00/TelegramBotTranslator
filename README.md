# Translator Telegram Bot DeepL

This bot was created with the purpose of introducing it in a telegram group between people who speak different language so that each of the messages sent is automatically translated into a desired language and English simultaneously. By default, the **detected language is Spanish** and the **translated language is Turkish** (in addition to English). 

## Prerequisites

First, it is neccesary to follow the common steps to create a Telegram Bot and adquire the Telegram API. Second, it is necesary to create a DeepL API account in order to adquire the DeepL API Token https://www.deepl.com/es/pro-api?cta=header-pro-api/.

It is also necesary to download the python packages: `requests` and `telegram.ext`.

## How it works

Let's imagine there is a Spanish-Turkish couple in which the Turk wants to learn Spanish. The Spaniard would write all the messages in Spanish and these would be automatically translated into Turkish and English so that the Turk can see the translation into his native language (in addition to English since it is a global language) and thus learn Spanish more easily.

To start the bot just use the command `/start` and to change the translated language use the command `/changelang <language-code>`.
>The language code has to be supported by DeepL API. See supported languages in https://support.deepl.com/hc/en-us/articles/360019925219-Languages-included-in-DeepL-Pro

>The language code has to be in format ISO 639-1. See language codes in http://utils.mucattu.com/iso_639-1.html

In addition, as indicated before, the **detected language** by default is Spanish. If you desire to change this language by any other language change the **source_lang** parameter:
```python
    data = {
        "auth_key": DEEPL_API_KEY,
        "text": message,
        "target_lang": language_pair,
        "source_lang": 'ES'
    }
```

Or if you prefer to let DeepL detect the source language, delete the parameter.

Finally, you will need to change this code:

```python
if ((chat.type == "" and chat.title == "") or
                (chat.type == "" and chat.first_name == "")):
```

This was coded so you can specify the group in which the bot will be used as we don't want it to be public so everyone uses our DeepL API calls.
>chat.type = private/group/supergroup... and chat.first_name corresponds to your name in case you want to use the bot in private.
