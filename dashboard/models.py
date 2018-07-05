from django.db import models

# Create your models here.

class OurGallery(models.Model):
    category=models.IntegerField(max_length=20)
    image = models.ImageField(upload_to="ourgallery", null=True, blank=True,
                              height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

class PhotoGallery(models.Model):
    desc = models.TextField(verbose_name="Brief Description:",max_length=200)
    image = models.ImageField(upload_to="photogallery", null=True, blank=True,
                              height_field="height_field", width_field="width_field",verbose_name="Select Photo:")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

class MediaGallery(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField(max_length=200,verbose_name="Brief Description:")
    image = models.ImageField(upload_to="mediagallery",
                              height_field="height_field", width_field="width_field",verbose_name="Select Image")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

class Testimonial(models.Model):
    comment=models.TextField(verbose_name='Enter Comment Here:')
    name=models.CharField(max_length=20)
    occupation=models.CharField(max_length=40)

class Blog(models.Model):
    title=models.CharField(verbose_name='Title',max_length=80)
    para1=models.TextField(verbose_name=' 1st Paragraph ')
    para2=models.TextField(verbose_name='2nd Paragraph',blank=True,null=True)
    image = models.ImageField(upload_to="blog", null=True, blank=True,
                              height_field="height_field", width_field="width_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    views = models.IntegerField(default=0)



class FreeCounselling(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
