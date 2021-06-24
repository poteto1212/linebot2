
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

#csrf認証

from django.views.decorators.csrf import csrf_exempt
#jsonファイル読み取り用
import json
#lineに対するコールバック用のメソッド

#linebotAPI用のモジュール
from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError


line_bot_api=LineBotApi('Li0swYw0GWbk1o7XzBF1KJLJ2/BV9n9nttEbuDsQdQi7AggHSmYL5w3Tsc+IUJ6fLHMa2DMj95oRww0W+DKJiBk978G2btHgqUO8wjs8dtJZJCjQjDks7sAsjK9rujXVvkBPmk77rtHjSLKfbWAi5QdB04t89/1O/w1cDnyilFU=')
#文字列Helloを返す
@csrf_exempt
def callback(request):
    sent_json=json.loads(request.body)
    reply_token=sent_json['events'][0]['replyToken']
    
    response['Content-Type']='application/json'
    response['Authorization']='Bearer Li0swYw0GWbk1o7XzBF1KJLJ2/BV9n9nttEbuDsQdQi7AggHSmYL5w3Tsc+IUJ6fLHMa2DMj95oRww0W+DKJiBk978G2btHgqUO8wjs8dtJZJCjQjDks7sAsjK9rujXVvkBPmk77rtHjSLKfbWAi5QdB04t89/1O/w1cDnyilFU='
    
    
    #try文で送信処理
    try:
        line_bot_api.reply_message(reply_token,TextSendMessage(text='HelloWorld'))
    except LineBotApiError as E:
        pass
    
    return response

urlpatterns = [
    path('admin/', admin.site.urls),
    path('callback/',callback)
]
