from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone

# Módulo de página: Conteúdo normal
'''class Section(models.Model):
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
        return self.text'''

# Homepage do portal #
class Homepage(models.Model):
    about = models.TextField()
    projects = models.TextField()
    # Áreas do curso
    health_informatics = models.TextField()
    bionformatics = models.TextField()

    contact = models.TextField()

    class Meta:
        verbose_name = 'Página inicial'
        verbose_name_plural = 'Página inicial'

    def __str__(self):
        return "Dados da Homepage"

# Informações sobre o curso #
class About(models.Model):
    what_is = models.TextField()
    acting = models.TextField()
    curricular_matrix = models.TextField()
    knowledge = models.TextField()

    class Meta:
        verbose_name = 'Sobre'
        verbose_name_plural = 'Sobre'

    def __str__(self):
        return "Dados sobre o curso"

class AreaBigCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Área mais genérica'
        verbose_name_plural = 'Área mais genérica'

class SpecificArea(models.Model):
    related_area = models.ForeignKey(AreaBigCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Área específica'
        verbose_name_plural = 'Área específica'

# Quadro de oportunidades #
class Opportunity(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    institution = models.CharField(max_length=150)
    city = models.CharField(max_length=100)
    area = models.CharField(max_length=150)
    created_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def approved_comments(self):
        return self.opportunitys.filter(approved_comment=True)
    
    class Meta:
        verbose_name = 'Oportunidade'
        verbose_name_plural = 'Oportunidades'

    def __str__(self):
        return self.title