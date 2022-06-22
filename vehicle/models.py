from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_instance(self):
        return self
    def __str__(self):
        return self.user.first_name

class Mechanic(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/MechanicProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    skill = models.CharField(max_length=500,null=True)
    salary=models.PositiveIntegerField(null=True)
    status=models.BooleanField(default=False)
    work_name = (('KSEB','KSEB'),('Other','Other'))
    work_category=models.CharField(max_length=50,choices=work_name)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

class Mechanic2(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/MechanicProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    skill = models.CharField(max_length=500,null=True)
    dis=(('Alappuzha','Alappuzha'),('Wayanad','Wayanad'),('Ernakulam','Ernakulam'),('Thrissur','Thrissur'),('Thiruvananthapuram','Thiruvananthapuram'),('Pathanamthitta','Pathanamthitta'),('Palakkad','Palakkad'),('Malappuram','Malappuram'),('Kozhikode','Kozhikode'),('Kottayam','Kottayam'),('Kollam','Kollam'),('Kasaragod','Kasaragod'),('Kannur','Kannur'),('Idukki','Idukki'))
    district = models.CharField(max_length=50,choices=dis)
    status=models.BooleanField(default=False)
    work_name = (('WATER AUTHORITY','WATER AUTHORITY'),('Other','Other'))
    work_category=models.CharField(max_length=50,choices=work_name)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name


class Request(models.Model):
    vehicle_name = (('Alappuzha','Alappuzha'),('Wayanad','Wayanad'),('Ernakulam','Ernakulam'),('Thrissur','Thrissur'),('Thiruvananthapuram','Thiruvananthapuram'),('Pathanamthitta','Pathanamthitta'),('Palakkad','Palakkad'),('Malappuram','Malappuram'),('Kozhikode','Kozhikode'),('Kottayam','Kottayam'),('Kollam','Kollam'),('Kasaragod','Kasaragod'),('Kannur','Kannur'),('Idukki','Idukki'))
    cat=(('Water authority','Water authority'),('KSEB','KSEB'))
    category=models.CharField(max_length=50,choices=cat)

    vehicle_no=models.PositiveIntegerField(null=False)

    
    vehicle_category=models.CharField(max_length=50,choices=vehicle_name)

    vehicle_model = models.CharField(max_length=40,null=False)
    vehicle_brand = models.CharField(max_length=40,null=False)

    problem_description = models.CharField(max_length=500,null=False)
    date=models.DateField(auto_now=True)
    cost=models.PositiveIntegerField(null=True)

    customer=models.ForeignKey('Customer', on_delete=models.CASCADE,null=True)
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)

    stat=(('Pending','Pending'),('Approved','Approved'),('Work in progress','Work in progress'),('Work Done','Work Done'),('Released','Released'))
    status=models.CharField(max_length=50,choices=stat,default='Pending',null=True)

    def __str__(self):
        return self.problem_description

class Attendance(models.Model):
    mechanic=models.ForeignKey('Mechanic',on_delete=models.CASCADE,null=True)
    date=models.DateField()
    present_status = models.CharField(max_length=10)

class Feedback(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=40)
    message=models.CharField(max_length=500)
