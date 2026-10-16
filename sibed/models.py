from django.db import models
#uma forma de controlar e manipular o banco de dados.Ex:criar uma tabela
#toda vez que alterar ou criar algo no modelo faça uma migration:
#python .\manage.py makemigrations [nome do app]

#tópico que se transformará em uma tabela que o usuário vai registrar no app para 
#inserir as anotações dele sobre aquele tópico


class Topic(models.Model):
    "um assunto sobre o qual o usuário está aprendendo"
    #atributo:campo no banco de dados
    #atributo    tipo      argumento
    text=models.charfield(max_lenght=200)
    #automaticamente vai preencer a data e a hora em que foi registrada alguma coisa.como um log
    date_added=models.DateTimeField(auto_now_add=True)
    #organiza os campos de forma esteticamente agradável
    def __str__(self):
        "devolve uma representação em string modelo"
        return self.text[:50]+"..."
