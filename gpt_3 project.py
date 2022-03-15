import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("API_KEY")

print("This will now initiate a casual convo with the gpt3 AI. ")

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful and clever.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
chat_log=None

def ask(question, chat_log): 
    prompt_text = f"{chat_log}{restart_sequence}:{question}{start_sequence}:"
    if chat_log is None: chat_log = session_prompt 
    response = openai.Completion.create(
        engine="ada",
        prompt= prompt_text,
        temperature=.95,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=["\n", " Human:", " AI:"]
    )
    computerAnswer=response.choices[0].text
    return computerAnswer

def append_interaction_to_chat_log(question, answer, chat_log):
    if chat_log is None: chat_log = session_prompt 
    return f"{chat_log}{restart_sequence} {question}{start_sequence}{answer}"
# ask user

while True:
    userInput=input("Enter 'y' to continue, 'q' to quit: ")

    if userInput=="q":
        break
    # chat log appending

    userInput=input("What would you like to ask the GPT3 chatbot?: ")
    # openai
    # second parameter is the response function : ask(userInput)

    computerAnswer= ask(userInput,chat_log)
    chat_log=append_interaction_to_chat_log(userInput, computerAnswer, chat_log)

    print(f"chat log: {chat_log} \n")


  


