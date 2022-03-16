from flask import Flask, redirect, render_template, url_for, request
from main_code import message, append_interaction_to_chat_log

app = Flask(__name__)
chat_log = None
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful and clever.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

@app.route('/')
def home():
    return render_template("chatbot.html")

@app.route('/https://danielliu122.github.io/openAI_Chatbot_basic/chat', methods=['GET', 'POST'])
def chat():
    global chat_log
    if chat_log is None: chat_log = session_prompt 
    userInput = request.form['user_input']
    Message=message(userInput, chat_log)[0]
    chat_log= append_interaction_to_chat_log(userInput, Message, chat_log)
    userInputLen=len(userInput)
    return '%s <br/> <br/> %s <br/> %s <br/> <br/>  <a href="/">Back Home</a>   ' % (Message , chat_log[:179] , chat_log[185:] )

    #return '%s  <br/> <a href="/">Back Home</a>' % (computerMessage)




if __name__ == "__main__":
	app.run(debug=True)
    