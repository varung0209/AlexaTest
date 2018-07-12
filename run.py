import os

from flask import Flask
from flask_ask import Ask, question, statement


app = Flask(__name__)
ask = Ask(app, "/")


@ask.launch
def launch():
    speech_text = 'Welcome To The Theta Protocol'
    return question(speech_text).reprompt(speech_text).simple_card('ThetaProtocol', speech_text)

@ask.intent('ThetaWorld')
def hello_world():
    speech_text = 'We See the World .......We Conquer it'
    return statement(speech_text).simple_card('ThetaProtocol', speech_text)

@ask.intent('ThetaMaster')
def hello_world():
    speech_text = 'Master Access = Archangel'
    return statement(speech_text).simple_card('ThetaProtocol', speech_text)

@ask.intent('ThetaSlave')
def hello_world():
    speech_text = 'All Mortals are Slaves'
    return statement(speech_text).simple_card('ThetaProtocol', speech_text)

@ask.session_ended
def session_ended():
    return "{}", 200


if __name__ == '__main__':
    if 'ASK_VERIFY_REQUESTS' in os.environ:
        verify = str(os.environ.get('ASK_VERIFY_REQUESTS', '')).lower()
        if verify == 'false':
            app.config['ASK_VERIFY_REQUESTS'] = False
    app.run(debug=True, port=5001)
