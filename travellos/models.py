from socket import setdefaulttimeout
from tarfile import StreamError
from django.db import models

# Create your models here.
class Destination(models.Model):

    name= models.CharField(max_length = 100)
    img= models.ImageField(upload_to='pics')
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)


class Interest(models.Model):
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title


class City(models.Model):
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=20)
    interests = models.ManyToManyField(Interest) #using many to many means that a person can have many interests
                                                 #and an interest can have many people.

    def __str__(self):
        return self.name


class PersonAdress(models.Model):
    person = models.OneToOneField(Person ,on_delete= models.CASCADE)# using one to one implies that one person can have an adress and an adress can have only one person
    city =  models.ForeignKey(City, on_delete=models.CASCADE)# the foreignkey implies that many people can have the same city but one person cant have more than one city hence making it a one to many 
    street_address = models.CharField(max_length = 200)

    def __str__(self):
        return self.person.name + "(" + self.street_address + ")" 

