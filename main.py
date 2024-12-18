from openai import OpenAI
from nextcord.ext import commands

# Initialize LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # LM Studio doesn't require an actual API key
)

# Initialize discord bot
bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}...')

@bot.slash_command(description="to know what model is being used", guild_ids=[TESTING_GUILD_ID])
async def model(interaction: nextcord.Interaction):
    await interaction.send("idk")

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

# discord token stuff
with open("secret.env", 'r') as env_file:
    env_data = env_file.readlines()
    KEY_DISCORD = env_data[0].strip()

# lm-studio function
def chat_with_lm_studio():
    model_identifier = "your-model-identifier"     

    print("Welcome to the LM Studio Chatbot!")
    print("Type 'exit' to end the conversation.")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        try:
            # Send the user's message to the model
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
        except Exception as e:
            print(f"An error occurred: {e}")

# # thign that do stuff
# if __name__ == "__main__":
#     chat_with_lm_studio()
