from django.views.generic import ListView, DetailView
from .models import UserMessage

class UserMessageList(ListView):
    model = UserMessage
    template_name = 'user_messages/user_message_list.html'
    context_object_name = 'user_messages'

class UserMessageDetail(DetailView):
    model = UserMessage
    template_name = 'user_messages/user_message_detail.html'
    context_object_name = 'user_message'
