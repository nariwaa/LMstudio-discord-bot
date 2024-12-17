from openai import OpenAI

# Initialize the client to point to LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1",
    api_key="lm-studio"  # LM Studio doesn't require an actual API key
)

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

if __name__ == "__main__":
    chat_with_lm_studio()
