from django.db import models

class Paste(models.Model):
    Python = 'Python'
    Javascript = 'Javascript'
    Outros = 'Outros'
    LINGUAGENS = (
        (Python, 'Python'),
        (Javascript, 'Javascript'),
        (Outros, 'Outros'),
    )
    titulo = models.CharField(max_length=200)
    linguagem = models.CharField(choices=LINGUAGENS, max_length=200)
    conteudo = models.TextField()
