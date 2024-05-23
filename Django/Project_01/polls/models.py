import datetime

from django.db import models
from django.utils import timezone

# Criação dos Modelos para o Banco de Dados


# Preparando o Banco para receber os Inputs
class Question(models.Model):
    tx_question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Função para exibição da própria classe
    def __str__(self):
        return self.tx_question

    # Função para retornar tempo de publicação da pergunta
    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=1))


# Preparando o Banco para receber os Outputs
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)        # Chave estrangeira
    tx_choice = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    # Função para exibição da própria classe
    def __str__(self):
        return self.tx_choice


