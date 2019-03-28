from flask import Flask, request, jsonify, render_template 
from slackclient import SlackClient
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
slack_token = 'xoxb-575060474148-585358061488-sKHNxUnHSwFO2qehLyEgWIZj'
sc = SlackClient(slack_token)



@app.route("/")
def index():
    return render_template("trail2.html")

@app.route("/send", methods=["POST"])
def send_message():
    message  = request.form['Message']
    print(message)
    sc = SlackClient(slack_token)
    sc.api_call(
        "chat.postMessage",
        channel = "@teamchat",
        text = message
    )

    return render_template("trail2.html")

if __name__ == '__main__':
    app.debug = True
    app.run()

