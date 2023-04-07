from django.core.validators import MaxValueValidator
from django.db import models

# Create your models here.
class entry(models.Model):
    name = models.CharField(max_length=25)
    # dob = models.DateField()
    # gender_choice = (
    #     ("male", "Male"),
    #     ("Female", "Female"),
    # )
    # gender = models.CharField( max_length=10)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField()
    address = models.CharField(max_length=25)
    address2 = models.CharField(max_length=25)
    post = models.PositiveIntegerField(validators=[MaxValueValidator(999999)])
    aadhar_card = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])
    ration_number = models.PositiveIntegerField(validators=[MaxValueValidator(9999999999)])

    # purpose_choice = (
    #     ("Enquiry", "Enquiry"),
    #     ("Apply", "Apply"),
    #     ("Complient", "Complient"),
    #     ("Others", "Others"),
    # )
    # purpose = models.CharField(max_length=100)

    def __str__(self):
        return self.name
