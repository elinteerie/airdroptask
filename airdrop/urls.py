from django.urls import path
from .views import airdrop_signup, success_view, user_info


urlpatterns = [
path('signup/', airdrop_signup, name='signup'),
path('success/', success_view, name='success'),
path('user/', user_info, name='user_info')
]
