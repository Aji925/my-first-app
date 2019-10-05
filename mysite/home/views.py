from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.template import RequestContext
from django.contrib import auth
from django.db import connection
from djongo import models
from django.db.models import Count
import hashlib,binascii,os #for hashing
# for rest-framework charts
from rest_framework.views import APIView  
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.views.generic import View

#current user
current_user = {'username':'','status':False}
# Create your views here.


def login(request):
    if request.method=='POST':
        uname=str(request.POST.get('username'))
        pswrd=str(request.POST.get('password'))
        login_user = list(user.objects.all().filter(username=uname).values())
        if len(login_user):
            if verify_passwordh(login_user[0]['password'],pswrd):
                current_user['username']=uname
                current_user['status']=True
                return redirect('home:home')
            else:
                return render(request,'home/login.html',{'error':'Incorrect password!'})
        else:
            return render(request,'home/login.html',{'error':'Username not found!'})
    else:
        return render(request,'home/login.html')


def logout(request):
    current_user['username']=''
    current_user['status']=False
    return redirect('home:login')

def home(request):
    if current_user['status'] or request.user.is_authenticated :
        return render(request,'home/homepage.html',)
    else:
        return redirect('home:login')

def profile(request):
    if current_user['status']:
        obj = list(user.objects.all().filter(username=current_user['username']).values_list())
        obj = [items for t in obj for items in t]
        print(obj)
        return render(request,'home/profile.html',{'username':obj[0],'fname':obj[2],'mname':obj[3],'lname':obj[4],'email':obj[5],'mobile':obj[6],'address':obj[7],'image':obj[8]})
    else:
        return redirect('home:login')
        
def signup(request):
    if request.method=='POST':
        user1=user()
        user1.username=request.POST.get('username')
        user1.password=hash_password(request.POST.get('password'))
        user1.fname=request.POST.get('fname')
        user1.mname=request.POST.get('mname')
        user1.lname=request.POST.get('lname')
        user1.email=request.POST.get('email')
        user1.address=request.POST.get('address')
        user1.mobile_no=request.POST.get('mobile')
        user1.profile_pic=request.POST.get('image')
        username_list=user.objects.values('username')#list of usernames
        if user1.username in username_list:
            return render(request,'home/signup.html',{'error':'Username already exists!'})
        else:
            user1.save()
            return redirect('home:login')
    else:
        return render(request,'home/signup.html',{})


# products views

def huawei_p30_pro(request):
    if request.method=='POST':
        if current_user['status']:
            p = Order()
            p.product_name='huawei_p30_pro'
            p.brand_name='huawei'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/huawei_p30_pro.html',{})

def motorola_one_vision(request):
    if request.method=='POST':
        if current_user['status']:
            p = Order()
            p.product_name='motorola_one_vision'
            p.brand_name='motorola'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/motorola_one_vision.html',{})

def nokia_4_2(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='nokia_4_2'
            p.brand_name='nokia'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/nokia_4_2.html',{})

def one_plus_7_pro(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='one_plus_7_pro'
            p.brand_name='one_plus'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/one_plus_7_pro.html',{})

def one_plus_7(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='one_plus_7'
            p.brand_name='one_plus'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/one_plus_7.html',{})

def oppo_reno_10x_zoom(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='oppo_reno_10x_zoom'
            p.brand_name='oppo'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/oppo_reno_10x_zoom.html',{})

def realme3_pro(request):
    if request.method=='POST':  
        if current_user['status']:
            p=Order()
            p.product_name='realme3_pro'
            p.brand_name='realme'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/realme3_pro.html',{})

def samsung_galaxy_a70(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='samsung_galaxy_a70'
            p.brand_name='samsung'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/samsung_galaxy_a70.html',{})

def samsung_galaxy_s10e(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='samsung_galaxy_s10e'
            p.brand_name='samsung'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/samsung_galaxy_s10e.html',{})

def xiaomi_redmi_k20_pro(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='xiaomi_redmi_k20_pro'
            p.brand_name='xiaomi'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/xiaomi_redmi_k20_pro.html',{})

def xiaomi_redmi_k20(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='xiaomi_redmi_k20'
            p.brand_name='xiaomi'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/xiaomi_redmi_k20.html',{})

def xiaomi_redmi_y3(request):
    if request.method=='POST':
        if current_user['status']:
            p=Order()
            p.product_name='xiaomi_redmi_y3'
            p.brand_name='xiaomi'
            p.bought_by=current_user['username']
            p.save()
            return render(request,'home/homepage.html',{'success':'Order successfully placed!'})
        else:
            return redirect('home:login')
    else:
        return render(request,'home/xiaomi_redmi_y3.html',{})



#hashing code

def hash_password(password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')
 
def verify_passwordh(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password



#charts view


class ChartView(View):
    def get(self,request,*args,**kwargs):
        return render(request,'home/charts.html',{})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self,request,format=None):
        brand_temp = list(Order.objects.values_list('brand_name').annotate(the_count=Count('brand_name')))
        brand_temp = [items for t in brand_temp for items in t]
        brand_names = brand_temp[::2]
        brand_count = brand_temp[1::2]
        data = {
            'labels' : brand_names,
            'chartData' : brand_count,
        }
        return Response(data)
