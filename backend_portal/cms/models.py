from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

# Módulo de página: Conteúdo normal
class Section(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    id_section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Content(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    #body = models.TextField()
    body = HTMLField('Content')
    author = models.CharField(max_length=100)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)
    expiration_date = models.DateField()
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_on']

# Módulo de post
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('cms.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, default='Anônimo')
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.text
