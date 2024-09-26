from django.db import models


# this model is how the data base will use the information aka the model, this model will create post on a webpage


class Post(models.Model):
    """Post model"""

    """text is the column in the data base"""
    text = models.TextField()

    def __str__(self):
        """string method"""
        return str(self.text)[:50]
