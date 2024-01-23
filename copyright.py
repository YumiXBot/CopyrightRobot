from pyrogram import Client, filters
import os
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import filters
from pyrogram.types import Message
import time
import psutil
import platform
# -------------------------------------------------------------------------------------

BOT_USERNAME = os.environ.get("BOT_USERNAME","NottyyXBot")

OWNER_ID = "6079943111"
# -------------------------------------------------------------------------------------

API_ID = "6435225" # 
API_HASH = "4e984ea35f854762dcde906dce426c2d"
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)

# --------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------

app = Client('my_bot', api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ----------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_txt = """<b> 🤖 𝖦𝗋𝗈𝗎𝗉 𝖲𝖾𝖼𝗎𝗋𝗂𝗍𝗒 𝖱𝗈𝖻𝗈𝗍 🛡️ </b>

𝖶𝖾𝗅𝖼𝗈𝗆𝖾 𝗍𝗈 𝖦𝗋𝗈𝗎𝗉𝖲𝖾𝖈𝗎𝗋𝗂𝗍𝗒𝖱𝗈𝖻𝗈𝗍, 𝗒𝗈𝗎𝗋 𝗏𝗂𝗀𝗂𝗅𝖺𝗇𝗍 𝗀𝗎𝖺𝗋𝖾𝗂𝗇 𝗂𝗇 𝗍𝗁𝗂𝗌 𝖳𝖾𝗅𝖾𝗀𝗋𝖺𝗆 𝗌𝗉𝖺𝖼𝖾! 𝖮𝗎𝗋 𝗆𝗂𝗌𝗌𝗂𝗈𝗇 𝗂𝗌 𝗍𝗈 𝖾𝗇𝗌𝗎𝗋𝖾 𝖺 𝗌𝖾𝖼𝗎𝗋𝖾 𝖺𝗇𝖽 𝗉𝗅𝖾𝖺𝗌𝖺𝗇𝗍 𝖾𝗇𝗏𝗂𝗋𝗈𝗇𝗆𝖾𝗇𝗍 𝖿𝗈𝗋 𝖾𝗏𝖾𝗋𝗒𝗈𝗇𝖾. 𝖥𝗋𝗈𝗆 𝖼𝗈𝗉𝗒𝗋𝗂𝗀𝗁𝗍 𝗉𝗋𝗈𝗍𝖾𝖼𝗍𝂢𝗂𝗈𝗇 𝗍𝗈 𝗆𝖺𝗂𝗇𝗍𝖺𝗂𝗇𝗂𝗇𝗀 𝖽𝖾𝖼𝗈𝗋𝗎𝗆, 𝗐𝖾'𝗏𝖾 𝗀𝗈𝗍 𝗂𝗍 𝖼𝗈𝗏𝖾𝗋𝖾𝖽.

𝖥𝖾𝖾𝗅 𝖿𝗋𝖾𝖾 𝗍𝗈 𝗋𝖾𝗉𝗈𝗿𝗍 𝖺𝗇𝗒 𝖼𝗈𝗇𝖼𝖾𝗋𝗇𝗌, 𝖺𝗇𝖽 𝗅𝖾𝗍'𝗌 𝗐𝗈𝗋𝗄 𝗍𝗈𝗀𝖾𝗍𝗁𝖾𝗋 𝗍𝗈 𝗆𝖺𝗄𝖾 𝗍𝗁𝗂𝗌 𝖼𝗈𝗆𝗆𝗎𝗇𝗂𝗍𝗒 𝗍𝗁𝗋𝗂𝗏𝖾! 🤝🔐 """

@app.on_message(filters.command("alonestart"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
          InlineKeyboardButton("• ʜᴀɴᴅʟᴇʀ •", callback_data="dil_back")
        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://graph.org/file/7f8ebddf56559ac69d31b.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )


gd_buttons = [              
        [
            InlineKeyboardButton("ᴏᴡɴᴇʀ", user_id=OWNER_ID),
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AloneXBots"),    
        ]
        ]


# ------------------------------------------------------------------------------- #


@app.on_callback_query(filters.regex("dil_back"))
async def dil_back(_, query: CallbackQuery):
    await query.message.edit_caption(start_txt,
                                    reply_markup=InlineKeyboardMarkup(gd_buttons),)
        

# -------------------------------------------------------------------------------------


# -------------------------------------------------------------------------------------


start_time = time.time()

def time_formatter(milliseconds: float) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return f"{int(hours)}h {int(minutes)}m {int(seconds)}s"

def size_formatter(bytes: int) -> str:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes < 1024.0:
            break
        bytes /= 1024.0
    return f"{bytes:.2f} {unit}"



@app.on_message(filters.command("ping"))
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    storage = psutil.disk_usage('/')

    python_version = platform.python_version()

    reply_text = (
        f"➪ᴜᴘᴛɪᴍᴇ: {uptime}\n"
        f"➪ᴄᴘᴜ: {cpu}%\n"
        f"➪ꜱᴛᴏʀᴀɢᴇ: {size_formatter(storage.total)} [ᴛᴏᴛᴀʟ]\n"
        f"➪{size_formatter(storage.used)} [ᴜsᴇᴅ]\n"
        f"➪{size_formatter(storage.free)} [ғʀᴇᴇ]\n"
        f"➪ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ: {python_version},"
    )

    await message.reply(reply_text, quote=True)


    
# -------------------------------------------------------------------------------------



@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_links_and_keywords(client, message):
    keywords = ["NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]
    
    if any(keyword.lower() in message.text.lower() for keyword in keywords) or any(link in message.text.lower() for link in ["http", "https", "www."]):
        await message.delete()
        
# -------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------
@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()



# ----------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------
@app.on_message(filters.group & filters.text & ~filters.me)
async def delete_long_messages(client, message):
    try:
        if len(message.text.split()) >= 10:

       
            print(f"Deleted message from {message.from_user.username}: {message.text}")
            
            
            await message.delete()
    except Exception as e:
        print(f"Error deleting message: {e}")
        
        
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

print(f"""╔═════❰𝐖𝐄𝐋𝐂𝐎𝐌𝐄❱════❍⊱❁۪۪║┏━━━━━━➣║┣⪼ ᴏᴡɴᴇʀ :- @DaxxSir3 ║┣⪼ ᴘᴀʀᴛ ᴏғ :- @ALLTYPECC║┗━━━━━━➣║╔═════ஜ۩۞۩ஜ════╗║अनंत अखंड अमर अविनाशी║कष्ट हरण है║शंभु कैलाशी║╚═════ஜ۩۞۩ஜ════╝╚═════════════════❍⊱❁ """)
app.run()
