from flask import Flask, redirect, render_template, url_for, request
from main_code import message, append_interaction_to_chat_log

app = Flask(__name__)
chat_log = None
session_prompt = "The following is a conversation with an AI assistant. The assistant is helpful and clever.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "

@app.route('/',methods=['GET','POST'])
def home():
    #global chat_log
    return render_template("chatbot.html")

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    global chat_log
    if chat_log is None: chat_log = session_prompt 
    userInput = request.form['user_input']
    engine_form = request.form['engine_type']
    if engine_form is not None:
        engine_type= engine_form
        print(engine_type)
    Message=message(userInput, chat_log, engine_type)[0]
    chat_log= append_interaction_to_chat_log(userInput, Message, chat_log)
    userInputLen=len(userInput)
    return '%s <br/> <br/> %s <br/> %s <br/> <br/>  <a href="/">Back Home</a>   ' % (Message , chat_log[:179] , chat_log[185:] )

    #return '%s  <br/> <a href="/">Back Home</a>' % (computerMessage)

@app.route('/clearChatlog')
def clearChatLog():
    global chat_log
    print("In clearChatLog")
    chat_log = None
    return "Nothing"


#background process happening without any refreshing
@app.route('/background_process_test')
def background_process_test():
    print ("Hello")
    return ("nothing")

if __name__ == "__main__":
	app.run(debug=True)
    