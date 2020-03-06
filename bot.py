from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/bot', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False
	if 'quote' in incoming_msg:
		print(incoming_msg)
		# r = requests.get('https://api.quotable.io/random')
		# if r.status_code==200:
		# 	data = r.json()
		# 	quote = f'{data["content"]}({data["author"]})'
		# else:
		# 	quote = 'I could not retrieve a quote at this time, sorry.'

		msg.body("Nahi milega koi quote")
		responded = True
	if 'bhejde' in incoming_msg:
		msg.body("kaha na nahi milega")
		responded = True
    	
	# if 'cat' in incoming_msg:
	# 	msg.media('https://cataas.com/cat')
	# 	responded = True
	# if not responded:
	# 	msg.body('I only know about famous quotes and cats, sorry!')
		
	return str(resp)

if __name__=="__main__":
	app.run(debug=True)
    	






    	
   
