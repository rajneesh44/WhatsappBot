# from flask import Flask, request
# import requests
# from twilio.twiml.messaging_response import MessagingResponse
# import ddg3

# app = Flask(__name__)

# # base = 'https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q='

# @app.route('/bot', methods=['POST'])
# def bot():
# 	incoming_msg = request.values.get('Body', '').lower()
# 	resp = MessagingResponse()
# 	msg = resp.message()
# 	responded = False

# 	r = ddg3.query(incoming_msg)
# 	print(incoming_msg)
	
# 	if r.type=='answer':
# 		res = r.results[0].text
# 		url = r.results[0].url
# 		msg.body(res+url)
# 		responded=True

# 	if r.type=='disambiguation':
# 		res = r.related[6].text
# 		url = r.related[0].url
# 		msg.body(res+url)
# 		responded=True

# 	if r.type=='nothing':
# 		res = r.answer.text
# 		# url = r.related[0].url
# 		msg.body(res)
# 		responded=True
# 	else:
# 		msg.body("Sorry! try something else")

# 	# res = r.related[2].text
# 	# print(r,res)
# 	# msg.body(res)
# 	# responded = True

		
# 	return str(resp)

# if __name__=="__main__":
# 	app.run(debug=True)
    	






    	
   


# from flask import Flask, request, session
# from twilio.twiml.messaging_response import MessagingResponse

# # The session object makes use of a secret key.
# SECRET_KEY = 'a secret key'
# app = Flask(__name__)
# app.config.from_object(__name__)

# # Try adding your own number to this list!
# callers = {
#     "+14158675308": "Rey",
#     "+12349013030": "Finn",
#     "+12348134522": "Chewy",
# }


# @app.route("/bot", methods=['GET', 'POST'])
# def bot():
#     """Respond with the number of text messages sent between two parties."""
#     # Increment the counter
#     counter = session.get('counter', 0)
#     counter += 1

#     # Save the new counter value in the session
#     session['counter'] = counter

#     from_number = request.values.get('From')
#     if from_number in callers:
#         name = callers[from_number]
#     else:
#         name = "Friend"

#     # Build our reply
#     message = '{} has messaged {} {} times.' \
#         .format(name, request.values.get('To'), counter)

#     # Put it in a TwiML response
#     resp = MessagingResponse()
#     resp.message(message)

#     return str(resp)


# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from chatterbot import ChatBot 
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)
chatbot = ChatBot('Ron Obvious')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    reply = chatbot.get_response(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    msg.body(str(reply))
    # responded = False
    # if 'quote' in incoming_msg:
    #     # return a quote
    #     r = requests.get('https://api.quotable.io/random')
    #     if r.status_code == 200:
    #         data = r.json()
    #         quote = f'{data["content"]} ({data["author"]})'
    #     else:
    #         quote = 'I could not retrieve a quote at this time, sorry.'
    #     msg.body(quote)
    #     responded = True
    # if 'cat' in incoming_msg:
    #     # return a cat pic
    #     msg.media('https://cataas.com/cat')
    #     responded = True
    # if not responded:
    #     msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)