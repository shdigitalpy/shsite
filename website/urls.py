from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('web-design', views.web_design, name="web_design"),
    path('web-entwicklung', views.web_entwicklung, name="web_entwicklung"),
    path('seo', views.seo, name="seo"),
    path('google-ads', views.google_ads, name="google_ads"),
    path('facebook-ads', views.facebook_ads, name="facebook_ads"),
    path('coaching', views.coaching, name="coaching"),
    path('online-kennzahlen', views.kennzahlen, name="online_kennzahlen"),
    path('digital-marketing-strategien', views.digital_marketing_strategien, name="digital_marketing_strategien"),
   	path('wer-wir-sind', views.wer_wir_sind, name="wer_wir_sind"),
   	path('send-modal/', views.SenderCreateView.as_view(), name="send_modal"),
   	path('ueber-uns', views.ueber_uns, name="ueber_uns"),
    path('kontakt', views.kontakt, name="kontakt")
]
