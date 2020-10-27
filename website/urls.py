from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('online-kennzahlen', views.kennzahlen, name="online_kennzahlen"),
    path('digital-marketing-strategien', views.digital_marketing_strategien, name="digital_marketing_strategien"),
   	path('wer-wir-sind', views.wer_wir_sind, name="wer_wir_sind"),
   	path('send-modal/', views.SenderCreateView.as_view(), name="send_modal")
]
