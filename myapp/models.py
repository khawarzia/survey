from django.db import models

class api_keys(models.Model):
    api_key = models.CharField(max_length=100)

    def __str__(self):
        return self.api_key
    
class form_submission(models.Model):
    form_type = models.CharField(max_length=100)
    name = models.CharField(max_length=300)
    phone_number = models.CharField(max_length=50)
    comments = models.TextField(max_length=2000)
    property_type = models.CharField(max_length=50)
    apartment_type = models.CharField(max_length=100)
    fav_district = models.CharField(max_length=1000)
    purpose = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name