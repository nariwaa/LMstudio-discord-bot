from openai import OpenAI

client = OpenAI(
    base_url="http://127.0.0.1:1434/v1/",
    api_key="whatever" # not needed
)

def main(pre_prompt="", user_name="user", ai_name="assistant", memory_limit=20):
    model_identifier = "llama3.2"     
    conversation_history = []

    print(f"Welcome to the {ai_name} Chatbot!")
    print("Type 'exit' to end the conversation.")

    if pre_prompt:
        conversation_history.append({"role": "system", "content": pre_prompt})

    while True:
        user_input = input(f"{user_name}: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        conversation_history.append({"role": "user", "content": user_input})

        if len(conversation_history) > memory_limit:
            conversation_history = conversation_history[-memory_limit:]

        try:
            completion = client.chat.completions.create(
                model=model_identifier,
                messages=conversation_history,
                temperature=0.7
            )

            response = completion.choices[0].message.content
            conversation_history.append({"role": "assistant", "content": response})
            print(f"{ai_name}: {response}")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main(
        pre_prompt="You are an assistant",
        user_name="user",
        ai_name="assistant",
        memory_limit=20
    )
