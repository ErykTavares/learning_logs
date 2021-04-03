from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    """Assunto que o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=CASCADE)

    def __str__(self):
        """Retonar um string do modelo"""
        return self.text


class Entry(models.Model):
    """Algo especifico de um assunto"""
    topic = models.ForeignKey(Topic, on_delete=CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta():
        verbose_name_plural = "entries"
        def __str__(self):
            return self.text[:50] + "..."


