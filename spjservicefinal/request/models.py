import uuid

from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models


# class Country(models.Model):
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name
#
#
# class City(models.Model):
#     country = models.ForeignKey(Country, on_delete=models.CASCADE)
#     name = models.CharField(max_length=40)
#
#     def __str__(self):
#         return self.name


class Person(models.Model):
    name = models.CharField(max_length=25)

    gender_choice = (
        ("male", "Male"),
        ("Female", "Female"),
    )
    gender = models.CharField(choices=gender_choice, max_length=10)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    post = models.IntegerField()
    aadhar_card = models.IntegerField()
    ration_number = models.IntegerField()
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)

    # country = models.ForeignKey(Country, on_delete=models.SET_NULL, blank=True, null=True)
    # city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    purpose_choice = (
        ("Enquiry", "Enquiry"),
        ("Apply", "Apply"),
        ("Complient", "Complient"),
        ("Others", "Others"),
    )
    purpose = models.CharField(max_length=100, choices=purpose_choice)


    def __str__(self):
        return self.name
