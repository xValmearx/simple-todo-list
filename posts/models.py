from django.db import models


class Post(models.Model):
    """Post model"""

    """text is the column in the data base"""
    text = models.TextField()
