from djongo import models
# Create your models here.

# user model 
class user(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    password=models.TextField()
    fname=models.CharField(max_length=50)
    mname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    mobile_no=models.BigIntegerField()
    address=models.TextField(default='')
    profile_pic=models.ImageField(upload_to='home/profile_img/',default='')

class Order(models.Model):
    product_name=models.CharField(max_length=50)
    brand_name=models.CharField(max_length=50,default='')
    bought_by=models.CharField(max_length=50)
    purchase_date=models.DateTimeField(auto_now_add=True)


objects = models.DjongoManager()