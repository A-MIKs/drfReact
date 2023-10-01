from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blog.models import *
from rest_framework.test import APIClient
from django.conf import settings
User = settings.AUTH_USER_MODEL

class PostTest(APITestCase):

    def test_view_post(self):
        url = reverse("blog_api:listcreate")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        self.test_category = Category.objects.create(name="django")
        self.testuser = User.objects.create_user(username="testuser", password="123456789")
        self.testuser.is_staff = True
        self.client.login(username=self.testuser.username, password="123456789")

        data = {"title":"new", "author":1, "excerpt":"new", "content":"new", "status":"published"}
        url = reverse("blog_api:listcreate")
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        root = reverse("blog_api:detailcreate", kwargs={"pk":1})
        response = self.client.get(root, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_update(self):
        client = APIClient()
        self.test_category = Category.objects.create(name="django")
        self.testuser1 = User.objects.create_user(username="testuser1", password="123456789")
        self.testuser2 = User.objects.create_user(username="testuser2", password="123456789")
        test_post = Post.objects.create(category_id=1, title="Post Title", excerpt="Post Excerpt", content="Post Content", slug="post-title", author_id=1, status="published")

        client.login(username=self.testuser1.username, password="123456789")
        root = reverse("blog_api:detailcreate", kwargs={"pk":1})
        data = {"title":"new", "author":1, "excerpt":"new", "content":"new", "status":"published"}
        response = client.put(root, data, format="json")
        print (response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)