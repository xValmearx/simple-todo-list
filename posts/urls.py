from django.urls import path

# for each page we create we need to specify it here

from posts.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
]
