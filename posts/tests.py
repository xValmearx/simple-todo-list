from django.test import TestCase
from django.urls import reverse


# reverse takes the home file and produces it as a url path

# Create your tests here.

from .models import Post


class PostTests(TestCase):
    """Post test"""

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        """Test the model content"""
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_exists_at_correct_location(self):
        """Test that ur; exist at the correct locaton"""

        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_avalible_by_name(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "This is a test!")
