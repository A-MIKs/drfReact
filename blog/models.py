from django.db import models
from django.conf import settings
from django.db.models.query import QuerySet
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
def upload_to(instance, filename):
    return "posts/{filename}".format(filename=filename)

class Post(models.Model):
    class PostObjects(models.Manager):
        def get_queryset(self) -> QuerySet:
            return super().get_queryset().filter(status="published")

    options = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    image = models.ImageField(_("Image"), upload_to=upload_to, default="posts/default.jpg")
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date="published")
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="blog_posts")
    status = models.CharField(max_length=10, choices=options, default="published")
    objects = models.Manager()
    postobjects = PostObjects()

    class Meta:
        ordering = ["-published"]

    def __str__(self):
        return self.title