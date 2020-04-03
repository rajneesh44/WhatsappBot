## This is a Chatbot made for whatsapp and it is now under maintainence.

The main purpose of this chatbot is to automate the conversation and make whatsapp a search engine as well, for the students.

## How to run:
```
1. First make a twilio account and go to programmable sms, click on whatsapp and go into the sandbox section.

2. Copy the phone number (+1 415 523 8886) on the sandbox page and there will be specific code like "join <something-something>". Copy it. Save the phone number and send the code for ex: join police-situation.

3. Make a virtual environment using python $virtualenv <env_name> 

4. $ pip install -r requirements.txt    #run this to install the requirements.

5. Run the main file by $python bot.py

6. your bot is now running on your server but not on your whatsapp. So now you have to install "ngrok" globally. $pip install ngrok.

7. Open a fresh terminal and type $ ngrok http 5000  few links will popup. Copy the web interface link and paste it in the "When a message comes in" column and add the "/bot" in the end of the link. and now you will be getting replies.
```

### References:
> [twilio](http://twilio.com/)
>[Chatterbot](https://github.com/gunthercox/ChatterBot/tree/0c4e38877a8a43458ac925444bb11d08aa5976fe)
>[ngrok](https://pypi.org/project/ngrok/)
>[Flask](https://pypi.org/project/Flask/)
>[Click here](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio) for more info regarding Whatsapp chatbot.
