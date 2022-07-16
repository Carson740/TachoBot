import hikari

bot = hikari.GatewayBot(token='OTk3ODc0OTMzMjk0MTc0MzU5.GAGC0h.id5-zr6NRoLHoTWKHde1oMBNjh2kd-fx7caqf0')
print("start")
@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)


bot.run()
