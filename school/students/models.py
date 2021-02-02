from django.db import models

# Create your models here.

class  user(models.Model):
    YEAR_IN_SCHOOL = {('G1', 'Grade1'),('G2','Grade2'),('G3','Grade3'), ('G4','Grade4'),('G5','Grade5'),('G6','Grade6'),('G7','Grade7'),('G8','Grade8'),('G9','Grade9'),('G10','Grade10')}
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_no = models.IntegerField(max_length=12)
    username = models.CharField(max_length=15)
    address = models.TextField()
    pincode = models.IntegerField()
    qualications = models.CharField(max_length=8,choices=YEAR_IN_SCHOOL,blank=True)
    class Meta():
        db_table='user'
       
class usertype(models.Model):
    
    type_enum = models.IntegerField()
    qualications = models.CharField(max_length=250)
    teaching_exp = models.CharField(max_length=500) 
    about_me = models.TextField()
    comments = models.TextField()
    class Meta():
        db_table='usertype'
      