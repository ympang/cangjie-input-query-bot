import telebot
import logging
import re
from config import TOKEN
from code_service import *

# Enable logging
logging.basicConfig(
    format="%(asctime)s | %(name)s | %(levelname)s | %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    new_message = f"""
你好，我可以幫你查倉頡碼（包括全型符號）。
亦支援一次過查多個文字（最多十個中文字）。
"""
    # bot.reply_to(message, new_message)
    bot.send_message(message.chat.id, new_message)


@bot.message_handler(commands=["test"])
def health_check(message):
    logger.info('health check')
    bot.send_message(message.chat.id, "正常運作中。。。")

# @bot.message_handler(content_types=['photo'])
# def handle_docs_audio(message):
#     logger.info(message)
#     file_id = message.photo[-1].file_id

#     bot.send_photo(message.chat.id, file_id)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # logger.info(message)
    result_list = []
    text = message.text
    bot_message = ""
    chi_text = re.findall(
        r"[\u4e00-\u9fff\u3000-\u3003\u3008-\u300F\u3010-\u3011\u3014-\u3015\u301C-\u301E\uFF0C-\uFF0E\uFE50-\uFE57\uFF1A\uFF1B\uFF1F\uFF01]+",
        text,
    )
    if len(chi_text) > 0:
        word_list = []
        for word in chi_text:
            word_list.extend(list(word))
        # remove duplicates and limit to 10 words
        word_list = list(dict.fromkeys(word_list))[:10]
        result_list = [
            {
                **{
                    "word": word,
                    "code": get_code(word),
                    "chi_code": get_chi_code_list(get_code(word)),
                }
            }
            for word in word_list
        ]
        for result in result_list:
            bot_message += f"""
{result['word']}
{str(result['code']).upper()}
倉頡碼：{result['chi_code']}
"""
    else:
        bot_message = "Diu no chinese"

    bot.send_message(message.chat.id, bot_message)


def main():
    logger.info("Bot Started.....")
    bot.infinity_polling()

if __name__ == "__main__":
    main()
