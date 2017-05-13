from django.db import models


class Room(models.Model):
    group = models.ForeignKey(Group)

    ownerName = models.ForeignKey(Person)
    participants = models.ManyToManyField(Person)

    moneyTotal = models.IntegerField()
    moneyRemain = models.IntegerField()

    created_date = models.DateTimeField(
            default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Group(models.Model):
    people = models.ManyToManyField(Person)

class Person(models.Model):
    name = models.CharField(max_length = 10)
    bank = models.CharField(max_length = 5)
    account = models.CharField(max_length = 20)

# Create your models here.
