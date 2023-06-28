import openai

def get_initial_message():
    messages=[
            {"role": "system", "content": "You are an expert in Nuclear Science and Power Generation. Who anwers brief questions about Nuclear Science and Power Generation. But Never Answer the question unrelated to Nuclear Science and Power Generation, instead reply to ask only about Nuclear Science and Power generation."},
            {"role": "user", "content": "I want to learn about Nuclear Energy Generation"},
            {"role": "assistant", "content": "Thats awesome, what do you want to know aboout Nuclear?"}
        ]
    return messages

def get_chatgpt_response(messages, model="gpt-3.5-turbo"):
    print("model: ", model)
    response = openai.ChatCompletion.create(
    model=model,
    messages=messages
    )
    return  response['choices'][0]['message']['content']

def update_chat(messages, role, content):
    messages.append({"role": role, "content": content})
    return messages
