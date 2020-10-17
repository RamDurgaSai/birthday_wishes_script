#This is the funny script that uses telegram (pyrogram) api to send reply 
#when some one wished through the telegram 








from pyrogram import Client,filters
from json import loads
from random import choice
import re,os


replies_list=(
    "Thank you very much for your kind and thoughtful birthday wishes.\
     You contributed so much in making my special day extra special. Much love!",
     "To have a friend like you greet me a happy bday first thing in the morning is something that I am thankful for. \
    Thanks for remembering my friend!",
    "To my friends, thank you so much for all the thoughtful words you have given me on my birthday.\
     Hugs and kisses for everyone!",
     "I really appreciate all you wonderful bday wishes !\
          I am so excited to party with you all! See you all later! No Party !",
    "Thanks for all the birthday wishes! You made a great day even greater!",
    "Thank you all for the wonderful birthday wishes. You guys are the best!",
    "You rock! Thanks for the birthday wishes, everyone!",
    "Thanks  for your birthday wishes. I can’t tell you how much I enjoyed hearing from so many friends.",
    "My thanks to you and who wished me a Happy Birthday . The rest of you are dead to me.",
    "Thanks for the birthday wishes, everyone. Hearing from you slightly lessened my despair at turning a year older.",
    "Thanks for all the wonderful birthday wishes, everyone. They almost made me forget that I’m speeding toward the grave.",
    "Thanks for all the Happy Birthday wishes, even the ones that teased me for being so old!",
    "Thanks for all the kind birthday wishes! The best birthday gift is being reminded of what wonderful friends I have!",
    "Thank you all for making me feel like a Super Hero on my birthday. Every single birthday wish was special to me.",
    "Thank you so much for the birthday wishes. Hearing from so many family members and friends makes me feel grateful for all the wonderful people in my life.",
    "Thanks for the sweet birthday wishes, everyone. They made me feel wonderful.",
    "Thank you all for the beautiful Happy Birthday wishes. You made my day extra-special."


)

telepot=Client("My Telepot",

                api_id=#  Replace with your api_id,
                api_hash=#Replace with your api hash)
team="1370636893"
@telepot.on_message(filters.chat(team) & filters.text)
def send_reply(client,message):
    print(message)



@telepot.on_message(filters.private & filters.text)
def send_reply(client,message):
    
    message_dic=loads(str(message))
    message_text=message_dic.get('text').lower()
   
    message_user_id=message_dic["from_user"]['id']

    message_user_name=message_dic["from_user"]['first_name']

    
    
    list=['happy','birthday','bday','wishing','wishes','returns']

    if message_user_name=="RamDurgaSai":
            return
        

    if re.compile('|'.join(list),re.IGNORECASE).search(message_text):

        message_reply=message.reply_text(text=choice(replies_list)+"\n\n Thanks . . . . .  "+
                                        str(message_user_name))
        

        telepot.send_sticker(chat_id=message_user_id,
                            sticker= "CAADAgADUgEAAjDUnRERwgZS_w81pBYE",
                            file_ref="AQAAXz1fiE7pIqT6ZvFTpNKD98VeYToCDA"  )

        print(message_user_name+" Is wished you ")
    else:
        return
        


telepot.run()





