import datetime
import requests
from will.plugin_base import WillPlugin
from will.decorators import respond_to, periodic, hear, randomly, route, rendered_template
import will.settings as settings


class FriendlyPlugin(WillPlugin):

    @respond_to("^hi")
    def hi(self, message):
        self.reply(message, "hello!")

    @hear("^(good )?(morning?)")
    def morning(self, message):
        self.say("mornin', %s" % message.sender.nick, message=message)

    @hear("^(good ?|g')?('?night)")
    def good_night(self, message):
        now = datetime.datetime.now()
        if now.weekday() == 4:  # Friday
            self.say("have a good weekend!", message=message)
        else:
            self.say("have a good night!", message=message)

