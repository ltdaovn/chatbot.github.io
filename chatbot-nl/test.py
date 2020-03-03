from rasa_core.agent import Agent
from rasa_core.interpreter import NaturalLanguageInterpreter
from rasa_core.utils import EndpointConfig

interpreter = NaturalLanguageInterpreter.create('./models/nlu/default/chat')
action_endpoint = EndpointConfig(url="http://localhost:5055/webhook")
agent = Agent.load('models/dialogue', interpreter=interpreter,action_endpoint=action_endpoint)
print("Your bot is ready to talk! Type your messages here or send 'stop'")
while True:
    print('user: ', sep=' ')
    a = input()
    if a == 'stop':
        break
    responses = agent.handle_text(a)
    print('agent: ', agent)
    print(responses)
    for response in responses:
        #print('bot: ',response["text"])
        print(response)