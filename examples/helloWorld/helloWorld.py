from pyastodon import Bot

from pyastodon.models.flags.scope import Scope


bot = Bot("botsin.space", Scope.READ | Scope.WRITE)
bot.logIn()
bot.toot("Hello, World!")