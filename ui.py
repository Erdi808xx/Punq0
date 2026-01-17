import discord

class PremiumEmbed(discord.Embed):
    def __init__(self, **kwargs):
        color = kwargs.pop("color", 0x9d4edd) # Default brand color
        super().__init__(color=color, **kwargs)
        self.set_footer(text="No.punq Premium Security")
        self.timestamp = discord.utils.utcnow()
