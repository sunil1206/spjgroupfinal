# from django.db import models
#
# # Create your models here.
# class entry(models.Model):
#     name = models.CharField(max_length=25)
#     # dob = models.DateField()
#     gender_choice = (
#         ("male", "Male"),
#         ("Female", "Female"),
#     )
#     gender = models.CharField(choices=gender_choice, max_length=10)
#     email = models.EmailField(max_length=100)
#     phone = models.IntegerField()
#     address = models.CharField(max_length=25)
#     address2 = models.CharField(max_length=25)
#     post = models.IntegerField()
#     aadhar_card = models.IntegerField()
#     ration_number = models.IntegerField()
#
#     purpose_choice = (
#         ("Enquiry", "Enquiry"),
#         ("Apply", "Apply"),
#         ("Complient", "Complient"),
#         ("Others", "Others"),
#     )
#     purpose = models.CharField(max_length=100, choices=purpose_choice)
#
#     def __str__(self):
#         return self.name