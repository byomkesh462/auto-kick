# @ Ayusman Bieb
from pyrogram import Client,filters
from .config import Config
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

bot=Client(":memory:",api_id=Config.TELEGRAM_APP_ID,api_hash=Config.TELEGRAM_APP_HASH,bot_token=Config.TELEGRAM_TOKEN)

@bot.on_message(filters.group | filters.channel | filters.new_chat_members)
def NewChat(bot, message):
    logging.info("New chat {}".format(message.chat.id))
    logging.info("Getting memebers from {}".format(message.chat.id))
    new_members = message.new_chat_members
    admins = bot.get_chat_members(message.chat.id, filter="administrators") 
    for new_mem in new_members:
        if new_mem in admins:
            logging.info("{} is an admin in {}".format(new_mem.user.id,message.chat.id))
            continue
        elif new_mem.id == bot.id:
            continue
        else:
            try:
                bot.get_chat_member(-1001513657958, new_mem.user.id)
                logging.info("{} is a member in {}".format(new_mem.user.id,message.chat.id))
            except Exception:
                bot.kick_chat_member(chat_id =message.chat.id,user_id=new_mem.user.id)
                logging.info("kicked {} from {}".format(new_mem.user.id,message.chat.id))
                logging.info(" failed to kicked {} from {}".format(i.user.id,message.chat.id))
            
    logging.info("process completed")
