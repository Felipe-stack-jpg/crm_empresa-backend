from django.db import models

STATUS_CHOICES = [
    ('andamento', 'Andamento'),
    ('concluido', 'Concluído'),
    ('cancelado', 'Cancelado'),
]

class Registro(models.Model):
    cliente = models.CharField(max_length= 255)
    produto = models.CharField(max_length= 255)
    numero_serie = models.CharField(max_length= 255, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='andamento')
    observacoes = models.TextField(blank=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.cliente} - {self.produto})"