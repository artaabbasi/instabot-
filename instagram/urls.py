from django.urls import path, include
from .views import * 

urlpatterns = [
    path('sendstory/', sendstory),
    path('sendpost/', sendpost),
    path('like_by_locations/', like_by_locations),
    path('like_by_tags/', like_by_tags),
    path('interact_user_likers/', interact_user_likers),
    path('interact_user_followers/', interact_user_followers),
    path('interact_user_following/', interact_user_following),
    path('interact_by_comments/', interact_by_comments),
]
