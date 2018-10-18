from django.db import models
from tinymce import HTMLField
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

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
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    text = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    #author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #@models.permalink
    def get_absolute_url(self):
        return ('blog_post_detail', (), 
                {
                    'slug' :self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)
    website = models.URLField(max_length=200, null=True, blank=True)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
