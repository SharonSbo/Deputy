from django.db import models

# Create your models here.
class DSE(models.Model):
    name= models.CharField(max_length=200)
    Role=models.CharField(max_length=100)
    Team= models.CharField(max_length=10, choices=[("Infra","Infra"),("app","App"),("security","Security")])
    Normalshifts=models.BooleanField()
    nightshifts =models.BooleanField()
    oncall= models.BooleanField()
    eveningshifts=models.BooleanField()
    ER=models.BooleanField()
    sundaymorning= models.BooleanField()
    earlyshifts= models.BooleanField()
    mondaytofriday=models.BooleanField()

    def __str__(self):
        return f"{self.name}"

