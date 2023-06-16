import openai
import random
import os

openai.api_key = 'API-KEY'  # Replace with your OpenAI API key

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10,
    )

    if response['choices'][0]['text']:
        return response['choices'][0]['text'].strip()
    else:
        return None

print("Enter 'quit' to exit.")

folder_path = r'C:\Users\jcsav\OneDrive\Desktop\Chatbot'  #Replace with the path to your folder

file_names = os.listdir(folder_path)
file_path = os.path.join(folder_path, random.choice(file_names))
file_name = os.path.splitext(os.path.basename(file_path))[0]

with open(file_path, 'r') as file:
    contexts = file.readlines()

context = random.choice(contexts).strip()
print(f"You are talking with {file_name}.")

conversation = []

while True:
    user_input = input("User: ")

    if user_input.lower() == 'quit':
        break

    conversation.append(f"You: {user_input}")
    prompt = ' '.join([context] + conversation + [f'\n{file_name}:'])

    response = chat_with_gpt(prompt)

    if response:
        print(f"{file_name}: {response}")
        conversation.append(f"{file_name}: {response}")
    else:
        print(f"{file_name}: I'm sorry, I didn't understand that. Can you please rephrase?")
