
from pyrogram import Client , filters

#---config---#
bot = {"api_id":API_ID, "api_hash": "API_HASH","token":"BOT_TOKEN","user":"@USERNAME_BOT","admin": "@USERNAME_ADMIN"}
#---------------#

#---clinet---#
app = Client(session_name="bot",api_id=bot["api_id"],api_hash=bot["api_hash"],bot_token=bot["token"])
#-------------#

user = bot["user"]
admin = bot["admin"]

#---start message---#
@app.on_message(filters.command(["start",f"start{user}"]) & filters.private)
def start_(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text("""
hello
wellcome to **Message Information robot**
this is bot for printing your message info
you can get help with send /help
""",quote=True)
#-------------------------#

#---inf part---#
@app.on_message(filters.command([f"inf{user}","inf"]) & filters.reply, group=1)
def info(c,m):
    c.send_chat_action(m.chat.id,"typing")
    if 4096 >= len(str(m)):
        m.reply_text(str(m)[:len(str(m))])
    elif 4097 <= len(str(m)) <= 8191:
        m.reply_text(str(m)[:4096])
        m.reply_text(str(m)[4096:len(str(m))])
    elif 8192 <= len(str(m)):
        m.reply_text(str(m)[:4096])
        m.reply_text(str(m)[4096:8192])
        m.reply_text(str(m)[8192:len(str(m))])
#-----------------#

#---info media---#
@app.on_message(filters.command([f"infmd{user}","infmd"]) & filters.reply, group=2)
def infmd(c,m):
    media = m.reply_to_message
    c.send_chat_action(m.chat.id,"typing")
    md = ["sticker","video","audio","animation","document","contact","voice","dice","game","video_note","poll","location"]
    for i in md:
        if media[i]:
            m.reply_text(media[i])
#----------------------#

#---info user---#
@app.on_message(filters.command(["infusr",f"infusr{user}"]) & filters.reply, group=3)
def infuse(c,m):
    c.send_chat_action(m.chat.id,"typing")
    usr = m.reply_to_message.forward_from
    if m.reply_to_message.forward_from:
        user = c.get_users(usr.id)
        m.reply_text(user)
    elif m.reply_to_message.forward_sender_name:
        m.reply_text("The guided message of the person is locked")
    else:
        m.reply_text("just forward message and reply this")
#-------------------#

#---info group---#
@app.on_message(filters.command(["infgp",f"infgp{user}"]) & filters.group, group=4)
def infgp(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text(m.chat)
#---------------------#

#---help---#
@app.on_message(filters.command(["help",f"help{user}"]) , group=5)
def help_(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text("""
━┅┅┈*┈┅┅━
Hello Robot guide message information

• Command /start to start or restart the robot

• The command /inf displays the message information **(you need to replay the message)**

• The command /infmd displays media information **(you must replay the message and also the message is media type, such as movies, photos, songs and ..)**

• The command /infusr gives half userName information **(you must forward a message from the person and replay it also should not be closed)**

• Command /infgp shows Group Information **(does not need to be replayed but must be sent in groups)**

• Command /admin to get admin ID 
You can use this to update the robot or provide the appropriate server or ... 
Support and you can also inform the robot's problems in this way
━┅┅┈*┈┅┅━
""")
#------------#

#---admin---#
@app.on_message(filters.command(["admin",f"admin{user}"]), group=6)
def admin(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text(f"id admin is :\n{admin}\nplease don't spam bot and don't flooding private message")
#---------------#

app.run()
