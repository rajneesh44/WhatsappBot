from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import ddg3

app = Flask(__name__)

# base = 'https://api.duckduckgo.com/?skip_disambig=1&format=json&pretty=1&q='

@app.route('/bot', methods=['POST'])
def bot():
	incoming_msg = request.values.get('Body', '').lower()
	resp = MessagingResponse()
	msg = resp.message()
	responded = False

	r = ddg3.query(incoming_msg)
	print(incoming_msg)
	
	if r.type=='answer':
		res = r.results[0].text
		url = r.results[0].url
		msg.body(res+url)
		responded=True

	if r.type=='disambiguation':
		res = r.related[6].text
		url = r.related[0].url
		msg.body(res+url)
		responded=True

	if r.type=='nothing':
		res = r.answer.text
		# url = r.related[0].url
		msg.body(res)
		responded=True

	# res = r.related[2].text
	# print(r,res)
	# msg.body(res)
	# responded = True

		
	return str(resp)

if __name__=="__main__":
	app.run(debug=True)
    	






    	
   
