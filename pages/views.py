# pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class HistoryPageView(TemplateView):
    template_name = 'pages/historia.html'

class PresentPageView(TemplateView):
    template_name = 'pages/ai_obecnie.html'

class PhilosophyPageView(TemplateView):
    template_name = 'pages/filozofia.html'

class ChatbotPageView(TemplateView):
    template_name = 'pages/chatbot.html'

class TalkPageView(TemplateView):
    template_name = 'pages/rozmowa.html'
