from flask import Flask, request, abort

from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import *

from engine.currency import currencySearch
from engine.InstagramFood import foodSearch
app = Flask(__name__)

# 設定你的Channel Access Token
line_bot_api = LineBotApi('+c7Vg1Hrv/Ggg9aZd6ksYDu1qM1e5N0nkea7X3GXnCxHxOxwLcBPJ8ySu0q1c7uoDOiXWlVE01e1y1hFkiIV0HLkdpe6KPCUztdAUbH4TAQhPgS48CqOAwmvlBlVtF7DP4BPa+BaPGhVi5fJs2sdMAdB04t89/1O/w1cDnyilFU=')
# 設定你的Channel Secret
handler = WebhookHandler('c7b36ec108800b95651bc0012468d250')
 
# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
	# get X-Line-Signature header value
	signature = request.headers['X-Line-Signature']
	# get request body as text
	body = request.get_data(as_text=True)
	app.logger.info("Request body: " + body)
	# handle webhook body
	try:
		handler.handle(body, signature)
	except InvalidSignatureError:
		abort(400)
	return 'OK'


#處理訊息
#當訊息種類為TextMessage時，從event中取出訊息內容，藉由TextSendMessage()包裝成符合格式的物件，並貼上message的標籤方便之後取用。
#接著透過LineBotApi物件中reply_message()方法，回傳相同的訊息內容

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
	userSend = event.message.text
	userID = event.source.user_id

	if userSend == 'Hi':
		message =TextSendMessage(text='Hi {}! 😯'.format(userID))
	elif userSend =='Food' or userSend =='food' or userSend =='食物':
		reply = foodSearch()
		replytext = ''
		for shop in reply:
			 replytext += shop
		message = TextSendMessage(text=replytext)
		
	elif userSend == 'Goodbye':
		message = TextSendMessage(text='See ya {}! 🙃'.format(userID))

	elif userSend in ['CNY', 'THB', 'SEK', 'USD', 'IDR', 'AUD', 'NZD', 'PHP', 'MYR', 'GBP', 'ZAR', 'CHF', 'VND', 'EUR', 'KRW', 'SGD', 'JPY', 'CAD', 'HKD']:
		message = TextSendMessage(text=currencySearch(userSend))	

	else:
		message = StickerSendMessage(package_id='11539', sticker_id='52114129')

	line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=StickerMessage)
def handle_message(event):
	print('執行StickerMessage')
	message = TextSendMessage(text='Sorry cannot truly tell what you want to talk about☹️')
	line_bot_api.reply_message(event.reply_token, message)



import os
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
