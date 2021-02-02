from django.db import models

# Create your models here.
#from django.contrib.auth.models import AbstractUser, BaseUserManager

#DEFAULT_USER_PASSWORD = 'admin123'

"""
# Consumer manager for Consumer Table
class ConsumerManager(BaseUserManager):

    def validate_phone_number(self, phone_number):
        phone_number = phone_number or ''
        if len(phone_number) >= 10:
            try:
                phone_number = int(phone_number)
                return phone_number
            except ValueError as e:
                raise ValueError('Phone number must be an integer')
        else:
            return False

    def create_user(self, phone_number, email=None, username=None, password=None):
        phone_number = self.validate_phone_number(phone_number)

        # Defaulting username and password
        if username is None:
            username = str(phone_number)
        if password is None:
            password = DEFAULT_USER_PASSWORD

        if not phone_number:
            raise ValueError("Users must have a valid phone number!")
        if not username:
            raise ValueError("Users must have username!")

        if email is not None:
            user = self.model(
                email=self.normalize_email(email),
                phone_number=phone_number,
                username=username,
            )
        else:
            user = self.model(
                phone_number=phone_number,
                username=username,
            )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, username, password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# Main User table
class Consumer(AbstractUser):
    email = models.EmailField(verbose_name="Email", max_length=100, null=True, blank=True)
    phone_number = models.CharField(verbose_name="Phone Number", max_length=15, unique=True)
    username = models.CharField(verbose_name="Username", max_length=50, unique=True)
    last_login = models.DateTimeField(verbose_name="last_login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    g_auth = models.CharField(verbose_name="google auth", max_length=200, unique=True, null=True, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["username"]

    objects = ConsumerManager()

    # def delete(self):
    #     self.is_active = False
    #     self.save()
    #     collector = Collector(using=None)
    #     return collector.delete()

    def __str__(self):
        return "{0} - {1}".format(self.id, self.phone_number)

    # def clean(self):
    #     if self.user_type == USER_TYPE_ID.get('Admin') and not self.is_admin:
    #         raise ValidationError({'user_type': 'Please select "Is admin" before selecting "Admin" user type'})
    #     if self.user_type != USER_TYPE_ID.get('CMDI') and self.user_type != USER_TYPE_ID.get("Contractor"):
    #         raise ValidationError(
    #             {'user_division': 'Only user type: CMDI or Contractor can be mapped to "User division"'})

    class Meta:
        db_table = "users"
"""

 #BHARATCHNAD
 #creating models data base 
"""
User	     	user type	board	standard	subject	org.	org centre
							
first name 		type(enum)	   board name 	class 1-12	subject name	org name 	
last name 		qualification	board logo 	board id	board id	org type 	org id
phone no 		teaching exp	board type(custom/default)		standard id	user id	header
email 		about me				no of students 	image/logo 
username 		comment				org logo 	footer
address						          org email	centre address
pincode						org website	
qualification						org customi	
						org address	
                        """
class User(models.Model):
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

    #def validate_phone_number(): //if it mobile  10 if its <10 or  >10 it must show error   and ladline number 12 if its <12 or >12 it must show error
    
    #def validate_email(): //It must have (example@mail.com ) and check the email in data base 

    #def validate_username()://it must have (8 char in abc...xyz ,including numbers  )
    #    
    class Meta: 
        db_table = "User"

class Usertype(models.Model):
    type_enum = models.CharField(max_length=20,blank=True)
    qualification = models.CharField(max_length=20,blank=True)
    #teaching_exp  = models.IntegerField(max_length=10,blank=False)
    teaching_exp  = models.CharField(max_length=10,blank=False) #If it is constance year of choices but having confusion for integerfiled  
    about_me = models.CharField(max_length=250, blank=True)
    comment = models.CharField(max_length=250, blank=True)

    #def validate_type_enum
     
    class Meta:
        db_table = "Usertype"

class Board(models.Model):
    BOARDCHOICES = {('ICSE board','ICSE'),('CBSE board','CBSE'),('State boards','State'),('IB','IB')}
    boardid = models.IntegerField(default=1,primary_key=True)
    board_name = models.CharField(max_length=100,blank=True) 
    board_logo  = models.ImageField()
    board_type = models.CharField(max_length=12,choices=BOARDCHOICES,blank=True,default=True)  #(custom/default)
    
    class Meta:
        db_table = "Board"

class Standard(models.Model):
    YEAR_IN_SCHOOL = {('G1', 'Grade1'),('G2','Grade2'),('G3','Grade3'), ('G4','Grade4'),('G5','Grade5'),('G6','Grade6'),('G7','Grade7'),('G8','Grade8'),('G9','Grade9'),('G10','Grade10'),('G11','Grade11'),('G12','Grade12')}
    stdid = models.IntegerField(default=1,primary_key=True)
    classs = models.CharField(max_length=8,choices=YEAR_IN_SCHOOL,blank=True)
    board_id = models.ForeignKey(Board,to_field="boardid",on_delete=models.CASCADE,null=True)        #(FK)
    class Meta:
        db_table = "Standard"

class Subjects(models.Model):
    subjectname  = models.CharField(max_length=100,blank=True)
    board_id  = models.ForeignKey(Board,to_field="boardid",on_delete=models.CASCADE,null=True)  #(FK) 
    standard_id = models.ForeignKey(Standard,to_field="stdid",on_delete=models.CASCADE,null=True)  #(FK)
    class Meta:
        db_table ='Subjects'

class Org(models.Model):
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

    class Meta: 
        db_table = 'Org'

class  Orgcenter(models.Model):
    org_id = models.ForeignKey(Org,to_field="orgid",on_delete=models.CASCADE,null=True) # (FK)
    header = models.CharField(max_length=500)
    image_logo = models.ImageField()
    footer = models.CharField(max_length=500,blank=True)
    centre_address = models.CharField(max_length=100,blank=True)
    
    class Meta:
        db_table = 'Orgcenter'
