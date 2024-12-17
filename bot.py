from nextcord.ext import commands

# the prefix is not used in this example
bot = commands.Bot(command_prefix='$')

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')

with open("secret.env", 'r') as env_file:
    env_data = env_file.readlines()
    KEY_DISCORD = env_data[0].strip()

bot.run(KEY_DISCORD)
