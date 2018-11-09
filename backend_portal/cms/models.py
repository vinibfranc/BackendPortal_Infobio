from django.db import models
from django.contrib.auth.models import User
from tinymce import HTMLField
#from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone
#from django.contrib import admin
#from adminfilters.models import Species, Breed

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
    title = models.CharField(max_length=150, verbose_name="título")
    description = models.TextField(verbose_name="descrição")
    institution = models.CharField(max_length=150, verbose_name="instituição")
    city = models.CharField(max_length=100, verbose_name="cidade")
    area = models.CharField(max_length=150, verbose_name="área")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="criado em")
    approved = models.BooleanField(default=False, verbose_name="Moderado")
    
    class Meta:
        verbose_name = 'Oportunidade'
        verbose_name_plural = 'Oportunidades'
        ordering = ['-approved', '-created_date']


    def __str__(self):
        return self.title