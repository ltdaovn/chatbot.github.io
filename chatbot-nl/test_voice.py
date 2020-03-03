from rasa_core.agent import Agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.utils import EndpointConfig
import time
import textToSpeech
import speechAnswer
import urllib.request
interpreter = NaturalLanguageInterpreter.create('./models/nlu/default/chat')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
cnt = 0
print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    cnt+=1
    print('user: ', end=' ')
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_text(a)
    print(responses)
    for response in responses:
        link_mp3 = textToSpeech.text_to_speech(response['text']) # convert string "answer" to file .mp3
        time.sleep(3) # wait for FPT server create link mp3
        try:
            urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(cnt) +'.mp3') # download file answer.mp3 from FPT server
        except:
            time.sleep(3)
            urllib.request.urlretrieve(link_mp3, 'mp3/answer'+ str(cnt) +'.mp3')
        speechAnswer.play_music('mp3/answer'+ str(cnt) +'.mp3', volume = 0.8) # play file "answer.mp3"
