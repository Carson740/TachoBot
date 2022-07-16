import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content == '!ping':
            await message.channel.send('bruh')

        if message.content.startswith("!cast"):
            channel = client.get_channel(997844570299711492)
            user = message.author.id
            cast = 997673917789519933
            print(message.content)
            echo = message.content.replace('!cast', '')
            msg = f"**<@{user}> has requested <@&{cast}>!\n\nIf you would like to apply to be cast, reply in the message thread!**" + "```" + echo + "```"
            await channel.send(msg)


client = MyClient()
client.run('OTk3ODc0OTMzMjk0MTc0MzU5.GAGC0h.id5-zr6NRoLHoTWKHde1oMBNjh2kd-fx7caqf0')