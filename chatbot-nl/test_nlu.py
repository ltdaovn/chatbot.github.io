from rasa_nlu.model import Interpreter

interpreter = Interpreter.load('./models/nlu/default/chat')

import sys
def main():
	if (len(sys.argv) > 1):
		print(interpreter.parse(sys.argv[1]))
main()
