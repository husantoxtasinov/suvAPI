from django.contrib.auth.models import User
from django.db import models

class Suv(models.Model):
    brend = models.CharField(max_length=50)
    narx = models.IntegerField()
    litr = models.IntegerField()
    batafsil = models.TextField()

    def __str__(self):return self.brend
class Mijoz(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    manzil = models.CharField(max_length=100)
    qarz = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):return self.ism
class Admin(models.Model):
    ism = models.CharField(max_length=50)
    yosh = models.PositiveIntegerField()
    ish_vaqti = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):return self.ism

class Haydovchi(models.Model):
    ism = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    kiritilgan_sana = models.DateField()
    def __str__(self):return self.ism
class Buyurtma(models.Model):
    suv = models.ForeignKey(Suv,on_delete=models.CASCADE)
    buyurtma_vaqti = models.DateField()
    mijoz = models.ForeignKey(Mijoz,models,on_delete=models.CASCADE)
    miqdor = models.IntegerField()
    umumiy_narx = models.IntegerField()
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE)
    haydovchi = models.ForeignKey(Haydovchi,on_delete=models.CASCADE)
    def __str__(self):return f"{self.suv},{self.mijoz},{self.admin},{self.haydovchi}"
