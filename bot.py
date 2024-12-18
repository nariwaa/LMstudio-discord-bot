from nextcord.ext import commands
import nextcord

TESTING_GUILD_ID = 1318201343382388837

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

# when message recived
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.content != "":
        print("not empty")
        # u should call the function
        await message.reply("dsofhiewhf")
    else:
        print("message empty, doing nothing")

with open("secret.env", 'r') as env_file:
    env_data = env_file.readlines()
    KEY_DISCORD = env_data[0].strip()

bot.run(KEY_DISCORD)
