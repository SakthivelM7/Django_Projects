from django.db import models

# Create your models here.
class Hero(models.Model):
    hero_name=models.CharField(max_length=150)

    def __str__(self):
        return self.hero_name

class Heroin(models.Model):
    heroin_name=models.CharField(max_length=150)
    def __str__(self):
        return self.heroin_name

class Director(models.Model):
    director_name=models.CharField(max_length=150)
    def __str__(self):
        return self.director_name

class Movie(models.Model):
    mov_name=models.CharField(max_length=150)
    hero_name=models.ForeignKey(Hero,on_delete=models.CASCADE)
    heroin_name=models.ForeignKey(Heroin,on_delete=models.CASCADE)
    director_name=models.ForeignKey(Director,on_delete=models.CASCADE)
    cost = models.IntegerField()
    def __str__(self):
        return self.mov_id

class Theater(models.Model):
    theater_name = models.CharField(max_length=150)
    def __str__(self):
        return self.theater_name

class Showtime(models.Model):
    mov_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater_name = models.ForeignKey(Theater, on_delete=models.CASCADE)
    datetime= models.DateTimeField()

class Customer(models.Model):
    Fname=models.CharField(max_length=150)
    Lname=models.CharField(max_length=150)
    Phno=models.BigIntegerField()
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class Booking(models.Model):
    mov_id=models.ForeignKey(Movie, on_delete=models.CASCADE)
    cust_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    No_of_seats= models.IntegerField()
    cost=models.IntegerField()







