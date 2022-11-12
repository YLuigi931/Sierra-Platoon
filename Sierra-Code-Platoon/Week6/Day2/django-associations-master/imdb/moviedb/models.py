from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=50)
    # roll = models.OneToOneField(Roll, null=True, related_name = "actor")

class Movie(models.Model):
    title = models.CharField(max_length=50)
    actors = models.ManyToManyField(Actor, related_name="movies", through="Role")
    

class Role(models.Model):
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE, related_name = "roles")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name = "roles")
