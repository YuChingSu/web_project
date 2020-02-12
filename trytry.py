import os
from flask import Flask, request, abort

from linebot import (
  LineBotApi, WebhookHandler
)
	
from linebot.exceptions import (
  InvalidSignatureError
)

from linebot.models import (
  MessageEvent, TextMessage, TextSendMessage, ImageMessage
)

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ.get('CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.environ.get('CHANNEL_SECRET'))

@app.route("/callback", methods=['POST'])
def callback():
  signature = request.headers['X-Line-Signature']
  body = request.get_data(as_text=True)
  app.logger.info("Request body: "+body)
  try:
    handler.handle(body,signature)
  except InvalidSignatureError:
    print("Invalid signature. Please check your channel access token/channel seceret.")
    abort(400)

  return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
  line_bot_api.reply_message(
    event.reply_token,
    TextSendMessage(text=event.message.text)
    )


if __name__ == "__main__":
  app.run()