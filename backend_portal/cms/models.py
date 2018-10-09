from django.db import models
from tinymce import HTMLField

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
    creation_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)
    expiration_date = models.DateField()
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['creation_date']

