
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

#lineに対するコールバック用のメソッド
#文字列Helloを返す
def callback(request):
    return HttpResponse('Hello')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('callback/',callback)
]
