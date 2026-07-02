from django.db import models
from django.contrib.auth.models import User

class ProgramaFidelidade(models.Model):
    nome = models.CharField(max_length=100, help_text="Ex: Smiles, ConnectMiles, Booking Genius")
    saldo_pontos = models.IntegerField(default=0)
    data_expiracao_proxima = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nome} - {self.saldo_pontos} pontos"

class Viagem(models.Model):
    titulo = models.CharField(max_length=200, help_text="Ex: Férias em Salvador, Viagem para Orlando")
    destino_principal = models.CharField(max_length=100)
    data_ida = models.DateField()
    data_volta = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50, choices=[
        ('planejada', 'Planejada'),
        ('em_andamento', 'Em Andamento'),
        ('concluida', 'Concluída')
    ], default='planejada')

    def __str__(self):
        return self.titulo

class TrechoTransporte(models.Model):
    viagem = models.ForeignKey(Viagem, on_delete=models.CASCADE, related_name='trechos')
    tipo = models.CharField(max_length=50, choices=[
        ('voo', 'Voo (Ex: GOL, Copa Airlines)'),
        ('onibus', 'Ônibus (Ex: Buser)'),
    ])
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    data_partida = models.DateTimeField()
    localizador = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.tipo} - {self.origem} para {self.destino}"