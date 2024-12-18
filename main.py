from openai import OpenAI
from nextcord.ext import commands
import nextcord

# Initialize LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # LM Studio doesn't require an actual API key
)

# Initialize discord bot
bot = commands.Bot()
TESTING_GUILD_ID = 1318201343382388837

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(description="to know what model is being used", guild_ids=[TESTING_GUILD_ID])
async def model(interaction: nextcord.Interaction):
    await interaction.send("idk")

# when message recived
@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.content != "":
        print("not empty")
        a = llm_message(f"{message.author}: {message.content}")
        await message.reply(a)
    else:
        print("message empty, doing nothing")

# discord token stuff
with open("secret.env", 'r') as env_file:
    env_data = env_file.readlines()
    KEY_DISCORD = env_data[0].strip()

# lm-studio function
def llm_message(user_input):
    model_identifier = "your-model-identifier"     

    try:
        completion = client.chat.completions.create(
            model=model_identifier,
            messages=[
                {"role": "user", "content": user_input}
            ],
            temperature=0.7  # Adjust creativity of responses
        )

        # Print the model's response
        response = completion.choices[0].message.content
        print(f"LM Studio: {response}")
        return(response)
    except Exception as e:
        print(f"An error occurred: {e}")
        return(f"An error occurred: {e}")

# thign that do stuff
if __name__ == "__main__":
    bot.run(KEY_DISCORD)
