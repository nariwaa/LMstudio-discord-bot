from openai import OpenAI
from nextcord.ext import commands
import nextcord

print("starting...")

# Initialize LM Studio
conversation_history = []
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # LM Studio doesn't require an actual API key
)

# Initialize discord bot
bot = commands.Bot()
TESTING_GUILD_ID = 1318201343382388837
BOT_ID = 1318202831131381760

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.slash_command(description="list every installed models", guild_ids=[TESTING_GUILD_ID])
async def model(interaction: nextcord.Interaction):
    modellist = [model.id for model in client.models.list().data]
    print(modellist)
    await interaction.send(modellist)

# when message received
@bot.event
async def on_message(message):
    print(f'Message from {message.author}({message.author.id}): {message.content}')
    if message.author.id != BOT_ID:
        if message.content != "":
            print("not empty")
            conversation_history.append({"role": "user", "content": message.content})
            a = llm_message()
            await message.reply(a)
        else:
            print("message empty, doing nothing")

# discord token stuff
with open("secret.env", 'r') as env_file:
    env_data = env_file.readlines()
    KEY_DISCORD = env_data[0].strip()

# lm-studio function
def llm_message():
    global conversation_history
    
    model_identifier = "your-model-identifier"     

    try:
        completion = client.chat.completions.create(
            model=model_identifier,
            messages=conversation_history,
            temperature=0.7  # Adjust creativity of responses
        )

        response = completion.choices[0].message.content
        print(f"LM Studio: {response}")
        
        # Add bot's message to history
        conversation_history.append({"role": "assistant", "content": response})
        
        # 10 message max
        if len(conversation_history) > 10:  # Example: keep last 10 interactions
            conversation_history = conversation_history[-10:]
        return response
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"

# thign that do stuff
if __name__ == "__main__":
    bot.run(KEY_DISCORD)
