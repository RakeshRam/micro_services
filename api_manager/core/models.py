from django.db import models

class Creator(models.Model):
    name = models.CharField(max_length=60)
    country = models.CharField(max_length=60)
    is_retired = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Ability(models.Model):
    ability = models.CharField(max_length=250)
    level = models.IntegerField(default=0)

    def __str__(self):
        return self.ability

class Character(models.Model):
    name = models.CharField(max_length=60)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    series = models.CharField(max_length=60, blank=True)
    team = models.CharField(max_length=60, blank=True)
    origin = models.CharField(max_length=30, blank=True)
    ability = models.ManyToManyField(Ability, related_name="superpowers")
    archenemy = models.ManyToManyField("self", blank=True)
    creator = models.ForeignKey(Creator, on_delete=models.CASCADE)
    is_villan = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

