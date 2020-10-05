# pages/urls.py
from django.urls import path
from .views import HomePageView, HistoryPageView, PresentPageView, PhilosophyPageView, ChatbotPageView, TalkPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('history/', HistoryPageView.as_view(), name='history'),
    path('present/', PresentPageView.as_view(), name='present'),
    path('philosophy/', PhilosophyPageView.as_view(), name='philosophy'),
    path('chatbot/', PhilosophyPageView.as_view(), name='chatbot'),
    path('talk/', PhilosophyPageView.as_view(), name='talk'),

]
