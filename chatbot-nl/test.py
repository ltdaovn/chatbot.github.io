from rasa_core.agent import Agent
from rasa_core.interpreter import NaturalLanguageInterpreter, RasaNLUInterpreter
from rasa_core.utils import EndpointConfig

interpreter = RasaNLUInterpreter('./models/nlu/default/chat')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    print('user: ', end='')
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_text(a)
    for response in responses:
        print('bot:',response["text"])