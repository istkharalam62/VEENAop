from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram import Client, filters, enums 

class BUTTONS(object):
    MBUTTON = [[InlineKeyboardButton("❃ ¢нαт-gρт ❃", callback_data="mplus HELP_ChatGPT"),InlineKeyboardButton("❃ gяσυρ ❃", callback_data="mplus HELP_Group"),InlineKeyboardButton("🦯 S͒T͒I͒C͒K͒E͒R͒ 🦯", callback_data="mplus HELP_Sticker")],
    [InlineKeyboardButton("❃ тαg-αℓℓ ❃", callback_data="mplus HELP_TagAll"),
    InlineKeyboardButton("❃ ιиfσ ❃", callback_data="mplus HELP_Info"),InlineKeyboardButton("❃ єχтяα ❃", callback_data="mplus HELP_Extra")],
    [InlineKeyboardButton("❃ ιмαgє ❃", callback_data="mplus HELP_Image"),
    InlineKeyboardButton("❃ α¢тισиѕ ❃", callback_data="mplus HELP_Action"),InlineKeyboardButton("❃ ѕєαя¢н ❃", callback_data="mplus HELP_Search")],    
    [InlineKeyboardButton("❃ fσит ❃", callback_data="mplus HELP_Font"),
    InlineKeyboardButton("❃ gαмє ❃", callback_data="mplus HELP_Game"),InlineKeyboardButton("❃ т-gяαρн ❃", callback_data="mplus HELP_TG")],
    [InlineKeyboardButton("❃ ιмρσѕтєя ❃", callback_data="mplus HELP_Imposter"),
    InlineKeyboardButton("❃ тяυтн∂αяє ❃", callback_data="mplus HELP_TD"),InlineKeyboardButton("❃ нαѕн-тαg ❃", callback_data="mplus HELP_HT")], 
    [InlineKeyboardButton("❃ ттѕ ❃", callback_data="mplus HELP_TTS"),
    InlineKeyboardButton("❃ fυи ❃", callback_data="mplus HELP_Fun"),InlineKeyboardButton("❃ qυιℓу ❃", callback_data="mplus HELP_Q")],          
    [InlineKeyboardButton("❃♡❃", callback_data=f"settings_back_helper"), 
    InlineKeyboardButton("❃♡❃", callback_data=f"managebot123 settings_back_helper"),
    ]]
