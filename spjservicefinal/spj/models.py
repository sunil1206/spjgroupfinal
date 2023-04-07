from django.db import models

# Create your models here.
class service(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=250)
    desc=models.TextField()
    detail=models.TextField()
    detail_img1=models.ImageField(upload_to='pics')
    detail_img2=models.ImageField(upload_to='pics')
    # detail=models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class about(models.Model):
    name = models.CharField(max_length=250)
    desc=models.CharField(max_length=750)

    def __str__(self):
        return self.name

class upcoming(models.Model):
    img=models.ImageField(upload_to='upcoming/pics')
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name
class upcoming2(models.Model):
    img=models.ImageField(upload_to='upcoming/pics')
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class upcoming3(models.Model):
    img=models.ImageField(upload_to='upcoming/pics')
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class slide(models.Model):
    name=models.CharField(max_length=250)
    desc=models.TextField(max_length=750)
    def __str__(self):
        return self.name

class client(models.Model):
    img=models.ImageField(upload_to='upcoming/pics')
    name=models.CharField(max_length=250)
    desc = models.TextField()
    def __str__(self):
        return self.name

class associate(models.Model):
    img=models.ImageField(upload_to='associate/pics')
    name=models.CharField(max_length=250)
    desc = models.TextField()
    def __str__(self):
        return self.name

# class gallery(models.Model):
#     vdo=models.FileField(upload_to='gallery/pics')
#     name=models.CharField(max_length=250)
#     desc = models.TextField()
#     def __str__(self):
#         return self.name

class gallery(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    desc = models.TextField()
    def __str__(self):
        return self.title
    # created_at = models.DateTimeField(auto_now_add=True)

class CarouselItem(models.Model):
    carousel_title = models.CharField(max_length=200 , blank=True, null=True)
    carousel_picture = models.ImageField(upload_to='carousel_images/', null=True, blank=True)

class gallery_foundation(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery')
    desc = models.TextField()
    def __str__(self):
        return self.title

