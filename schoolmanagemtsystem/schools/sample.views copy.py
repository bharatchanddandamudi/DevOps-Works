from django.shortcuts import render
from .import models 
from rest_framework.parser import 
# Create your views here.


def User():
    userid = models.IntegerField(default=1,primary_key=True)
    first_name = models.CharField(max_length=100,blank=True)
    last_name  = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    email = models.EmailField(max_length=250, blank=False, unique=True,
        error_messages={'required': 'Please provide your email address.',
                        'unique': 'An account with this email exist.'})
    username = models.CharField(max_length=20,blank=True)
    address = models.CharField(max_length=250,blank=False)
    pincode = models.CharField(max_length=8,blank=True)
    qualification = models.CharField(max_length=20,blank=True)

  
def  Usertype((models.Model):
    type_enum = models.CharField(max_length=20,blank=True)
    qualification = models.CharField(max_length=20,blank=True)
    #teaching_exp  = models.IntegerField(max_length=10,blank=False)
    teaching_exp  = models.CharField(max_length=10,blank=False) #If it is constance year of choices but having confusion for integerfiled  
    about_me = models.CharField(max_length=250, blank=True)
    comment = models.CharField(max_length=250, blank=True)


def  Board(models.Model):
    BOARDCHOICES = {('ICSE board','ICSE'),('CBSE board','CBSE'),('State boards','State'),('IB','IB')}
    boardid = models.IntegerField(default=1,primary_key=True)
    board_name = models.CharField(max_length=100,blank=True) 
    board_logo  = models.ImageField()
    board_type = models.CharField(max_length=12,choices=BOARDCHOICES,blank=True,default=True)  #(custom/default)
    
   

def  Standard(models.Model):
    YEAR_IN_SCHOOL = {('G1', 'Grade1'),('G2','Grade2'),('G3','Grade3'), ('G4','Grade4'),('G5','Grade5'),('G6','Grade6'),('G7','Grade7'),('G8','Grade8'),('G9','Grade9'),('G10','Grade10'),('G11','Grade11'),('G12','Grade12')}
    stdid = models.IntegerField(default=1,primary_key=True)
    def s = models.CharField(max_length=8,choices=YEAR_IN_SCHOOL,blank=True)
    board_id = models.ForeignKey(Board,to_field="boardid",on_delete=models.CASCADE,null=True)        #(FK)
   

def  Subjects(models.Model):
    subjectname  = models.CharField(max_length=100,blank=True)
    board_id  = models.ForeignKey(Board,to_field="boardid",on_delete=models.CASCADE,null=True)  #(FK) 
    standard_id = models.ForeignKey(Standard,to_field="stdid",on_delete=models.CASCADE,null=True)  #(FK)
    

def  Org(models.Model):
    orgid = models.IntegerField(default=1,primary_key=True)
    org_name = models.CharField(max_length=100,blank=True)
    org_type = models.CharField(max_length=100,blank=True)
    user_id = models.ForeignKey(User,to_field="userid",on_delete=models.CASCADE,null=True)  #(FK) 
    no_of_students = models.IntegerField()
    org_logo  = models.IntegerField()
    org_email = models.EmailField(max_length=100,blank=True)
    org_website = models.URLField()
    org_customi = models.CharField(max_length=100,blank=True)
    org_address = models.CharField(max_length=250, blank=True)

    

def   Orgcenter(models.Model):
    org_id = models.ForeignKey(Org,to_field="orgid",on_delete=models.CASCADE,null=True) # (FK)
    header = models.CharField(max_length=500)
    image_logo = models.ImageField()
    footer = models.CharField(max_length=500,blank=True)
    centre_address = models.CharField(max_length=100,blank=True)
    
   