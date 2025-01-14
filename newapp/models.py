from django.db import models

class api_keys(models.Model):
    api_key = models.CharField(max_length=100, unique=True)
    allowed = models.BooleanField(default=True)

    def __str__(self):
        return self.api_key
    
class form_submission(models.Model):
    form_type = models.CharField(max_length=10,null=True,blank=True)
    name = models.CharField(max_length=300,null=True,blank=True)
    phone_number = models.CharField(max_length=20,null=True,blank=True)
    comments = models.TextField(max_length=2000,null=True,blank=True)
    property_type = models.CharField(max_length=50,null=True,blank=True)
    apartment_type = models.CharField(max_length=10,null=True,blank=True)
    fav_district = models.CharField(max_length=250,null=True,blank=True)
    purpose = models.CharField(max_length=10,null=True,blank=True)
    submission_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def getFormType(self):
        if self.form_type == "1":
            return "Renting"
        return "Buying"
    
    def getPropertyType(self):
        if self.property_type == "1":
            return "Land"
        if self.property_type == "2":
            return "Apartment"
        if self.property_type == "3":
            return "House"
        if self.property_type == "4":
            return "Floor"
        if self.property_type == "5":
            return "Studio"
        if self.property_type == "6":
            return "Store"
        return self.property_type
    
    def getApartmentType(self):
        if self.apartment_type == "1":
            return "2 Bedrooms"
        if self.apartment_type == "2":
            return "2 Bedrooms + 1 Living Room"
        if self.apartment_type == "3":
            return "3 Bedrooms + 1 Living Room"
        if self.apartment_type == "4":
            return "Open to options"
        return ""
    
    def getPurpose(self):
        if self.purpose == "1":
            return "Family"
        if self.purpose == "2":
            return "Bachelor"
        return ""
