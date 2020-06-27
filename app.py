from flask import Flask, request
# from chatbot import bot_response
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/')
def hello_chatbot():
	question = request.values.get('Body', 'Hello')
	#answer = bot_response(question)
	answer = "Hello to you!"
	# init twilio response object
	response = MessagingResponse()
	# create message to send to twilio
	response.message(answer)

	return str(response)


if __name__ == '__main__':
	app.run(debug=True)