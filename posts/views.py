from django.views.generic import ListView
from posts.models import Post


class HomePageView(ListView):
    """Home Page View"""

    # after defining the model here django will do magic from the ListView to create post_list, it will take Post and make it lower case
    # post_list will automatically fetch all Post in the Data Base

    # gets the modle we want to use, basically be able to make post on the page
    model = Post

    # use the home.html template
    template_name = "home.html"
