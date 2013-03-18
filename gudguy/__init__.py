from irctk import Bot

from gudguy.config import Config

# initialize the bot
bot = Bot()
bot.config.from_object(Config)

# load the plugins
from gudguy import giphy, sc, youtube

