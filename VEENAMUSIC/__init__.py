from VEENAMUSIC.core.bot import VEENA
from VEENAMUSIC.core.dir import dirr
from VEENAMUSIC.core.git import git
from VEENAMUSIC.core.userbot import Userbot
from VEENAMUSIC.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = VEENA()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
