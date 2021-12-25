import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hai {}!!</b>
<i>I'm Simple Auto file Forward Bot V2
This Bot forward all files to One Public channel to Your Personal channel
More details /help</i>"""
  CAPTION = "`{}`\n\n" + str(Config.CAPTION)
  HELP_TXT = """<b>Follow These Steps!!
• User Join From channel Must(No need Admin permission)
• Then give admin permission in your personal telegram channel
• Then use /run command in your bot</b>

<b><u>Available Command</b></u>

* /start - <i>Bot Alive</i>
* /help - <i>more help</i>
* /run - <i>start forward</i>
* /about - <i>About Me</i>
* /restart - <i>Server Restart</i>"""
  ABOUT_TXT = """<b><u>My Info</b></u>

<b>Name :</b> <code>Auto Forward Bot</code>
<b>Credit :</b> <code>Dark Angel</code>
<b>Language :</b> <code>Python3</code>
<b>Lybrary :</b> <code>Pyrogram v1.2.9</code>
<b>Server :</b> <code>Heroku</code>
<b>Build :</b> <code>V2.0</code>"""
  FROM_MSG = "<b><u>SET FROM CHANNEL USERNAME</b></u>\n<b>Enter From Channel Username</b>\n<code>eg: @username</code>\n/cancel <code>- Cancel this process</code>"
  TO_MSG = "<b><u>SET TO CHANNEL ID</b></u>\n<b>Enter To Channel id</b>\n<code>eg: -100xxxxxxxxxx</code>\n/cancel <code>- Cancel this process</code>"
  SKIP_MSG = "<b><u>SET FILE SKIPING NUMBER</b></u>\n<b>Skip the file as much as you enter the number and the rest of the file will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 file skiped\n You enter 5 = 5 file skiped</code>\n/cancel <code>- Cancel this process</code>"
  LIMIT_MSG = "<b><u>SET FILE FORWARD LIMIT</u></b>\n<b>Heroku Daily Limit</b> : <code>23000</code>\n<b>Default Limit</b> : <code>0</code>"
  CANCEL = "<b>Process Cancelled Succefully\nEnter /run Again</b>"
  USERNAME = "<b>Send Username with @</b>\n<code>eg: @Username</code>\n<b>Enter /run Again</b>"
  INVALID_CHANNELID = "<b>Send channel id with -100</b>\n<code>eg: -100xxxxxxxxxx</code>\n<b>Enter /run Again</b>"
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the file Click the Yes button only after checking the following</code>

<i>° Must be a user join in From channel check that status</i>
<i>User join this channel : <b>{}</b></i>
<b><u>Note</u></b> : <i>Admin permission is not mandatory</i>
<i>° Admin permission is mandatory for the bot on the To channel check that status</i>
<b><u>Note</u></b> : <i>There is no requirement for a user to join the To channel</i>

<b>If the above is checked then the yes button can be clicked</b>"""
