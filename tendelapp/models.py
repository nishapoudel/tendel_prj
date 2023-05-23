from django.db import models
# from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

from datetime import datetime, date
from django.urls import  reverse


from django.db.models import F


class IpModel(models.Model):
    ip = models.CharField(max_length=100)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    country = models.CharField(max_length=255,null=True)

    def __str__(self):
        return self.ip

class Item(models.Model):
    item_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    image = models.ImageField(upload_to='post/',default='default.jpg')
    brand= models.CharField(max_length=100,blank=True)
    publish=models.BooleanField()

    views = models.ManyToManyField(IpModel, related_name = "post_views",blank=True)# add this field to track views


    class Meta:
        ordering=['-item_id']

    def __str__(self):
        return self.title


class Branch(models.Model):
    branch_id =models.AutoField(primary_key=True)
    main_address = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    phone =  PhoneNumberField(blank=True )

    manager_name=models.CharField(max_length=100)
    manager_contact=models.CharField(max_length=100)
    manager_email=models.EmailField(max_length = 254)
    map_link = models.URLField(default=" https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3534.894034741719!2d85.52059027426827!3d27.62779832899771!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x39eb09c614ab615f%3A0x6af270ba59691ae8!2sTENDEL%20Hardware%20Pvt.Ltd!5e0!3m2!1sen!2snp!4v1684647619175!5m2!1sen!2snp ",max_length=500)


    class Meta:
        ordering=['-branch_id']



    def __str__(self):
        return self.main_address

class News(models.Model):
    news_id =models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=100)
    name = models.CharField(max_length=100)




    class Meta:
        ordering=['-news_id']


    def __str__(self):
        return self.body


class Gallery(models.Model):
    gallery_id =models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='gallery/',default='default.jpg')

    class Meta:
        ordering=['-gallery_id']

class Offer(models.Model):
    offer_id =models.AutoField(primary_key=True)
    discount = models.CharField(max_length=100)
    validtime = models.CharField(max_length=100)




    class Meta:
        ordering=['-offer_id']


class Team(models.Model):
    team_id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/',default='default.jpg')




    class Meta:
        ordering=['-team_id']


    def __str__(self):
        return self.name


