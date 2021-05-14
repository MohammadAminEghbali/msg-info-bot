from pyrogram import Client , filters
import os

#---config---#
bot = {"api_id":3674694, "api_hash": "0e4b9ef7b55458d0fef367259edee34c","token":"1855543448:AAGKuF0jboFQ81O086luNHdq8wVmEfG1D88"}
#---------------#

#---clinet---#
app = Client(session_name="bot",api_id=bot["api_id"],api_hash=bot["api_hash"],bot_token=bot["token"])
os.system("clear")
#-------------#

#---start message---#
@app.on_message(filters.command(["start","start@msg_infobot"]) & filters.private)
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
@app.on_message(filters.command(["inf@msg_infobot","inf"]) & filters.reply, group=1)
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
@app.on_message(filters.command(["infmd@msg_infobot","infmd"]) & filters.reply, group=2)
def infmd(c,m):
    media = m.reply_to_message
    c.send_chat_action(m.chat.id,"typing")
    md = ["sticker","video","audio","animation","document","contact","voice","dice","game","video_note","poll","location"]
    for i in md:
        if media[i]:
            m.reply_text(media[i])
#----------------------#

#---info user---#
@app.on_message(filters.command(["infusr","infusr@msg_infobot"]) & filters.reply, group=3)
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
@app.on_message(filters.command(["infgp","infgp@msg_infobot"]) & filters.group, group=4)
def infgp(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text(m.chat)
#---------------------#

#---help---#
@app.on_message(filters.command(["help","help@msg_infobot"]) , group=5)
def help_(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text("""
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

سلام راهنمای ربات اطلاعات پیام

• دستور
/start
برای شروع یا راه اندازی مجدد ربات

• دستور
/inf
اطلاعات پیام را نمایش میدهد **(باید روی پیام ریپلای کنید)**

• دستور
/infmd
اطلاعات مدیا را نمایش میدهد **(باید روی پیام ریپلای کنید و همچنین پیام از نوع مدیا باشد مثل فیلم ، عکس ، آهنگ و ..)**

• دستور
/infusr
اطلاعات یوزر نیم را میدهد **(باید پیامی از شخص فوروارد کنید و روی آن ریپلای کنید همچنین نباید فوروارد شخص بسته باشد)**

• دستور
/infgp
اطلاعات گروه را نشان میدهد **(نیازی به ریپلای ندارد ولی حتما باید در گروه ها ارسال شود)**

• دستور 
/admin
 برای دریافت آیدی مدیر است 
شما میتوانید از این طریق ربات را برای به روزرسانی های جدید یا تهیه سرور مناسب یا ... 
حمایت کنید و همچنین میتوانید مشکلات ربات را از این طریق اطلاع رسانی کنید
""")
#------------#

#---admin---#
@app.on_message(filters.command(["admin","admin@msg_infobot"]), group=6)
def admin(c,m):
    c.send_chat_action(m.chat.id,"typing")
    m.reply_text("id admin is :\n@h_app_y\nplease don't spam bot and don't flooding private message")
#---------------#
app.run()
