from django.db import models
#from django.contrib.postgres.fields import ArrayField
#from django_pg import models

class Secao(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    id_secao = models.ForeignKey(Secao, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Conteudo(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    corpo = models.TextField()
    autor = models.CharField(max_length=100)
    data_criacao = models.DateField(auto_now_add=True)
    data_alteracao = models.DateField(auto_now=True)
    data_expiracao = models.DateField()
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['data_criacao']


'''class InformacoesUfcspa(models.Model):
    descricao = models.TextField()
    infraestrutura = models.TextField()
    cursos = models.TextField()

TIPOS_BOLSAS = (
    ('ic', 'ic'),
    ('iti', 'iti'),
    ('unasus', 'unasus')
)

# Seção de quadro de oportunidades
class Bolsa(models.Model):
    descricao = models.TextField()
    tipo = models.CharField(max_length=20, choices=TIPOS_BOLSAS)

class Estagio(models.Model):
    descricao = models.TextField()
    instituicao = models.CharField(max_length=50)
    tema = models.CharField(max_length=50)

class ProjetoPesquisa(models.Model):
    descricao = models.TextField()
    orientador = models.CharField(max_length=50)
    #participantes = models.ArrayField(models.CharField(max_length=50))
    participantes = models.TextField()
    areas = models.TextField()

# Seção de comparação de cursos
class Curso(models.Model):
    descricao = models.TextField()
    perfil_aluno = models.TextField()
    grade_curricular = models.FileField()
    diferenciais = models.TextField()

# Seção de infográficos
class Habilidades(models.Model):
    socio_culturais = models.TextField()
    humanitarias = models.TextField()
    tecnicas = models.TextField()

class AtuacaoProfissional(models.Model):
    empresas = models.TextField()
    areas_atuacao = models.TextField()'''