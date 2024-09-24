from django.db import models


class Post(models.Model):
    """Post model"""

    """text is the column in the data base"""
    text = models.TextField()

    def __str__(self):
        """string method"""
        return str(self.text)[:50]
