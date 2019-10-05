from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('home/',views.home,name='home'),
    path('',views.home,name='home'),
    path('profile/',views.profile,name='profile'),
    path('signup/',views.signup,name='signup'),
    path('huawei_p30_pro/',views.huawei_p30_pro,name='huawei_p30_pro'),
    path('motorola_one_vision/',views.motorola_one_vision,name='motorola_one_vision'),
    path('nokia_4_2/',views.nokia_4_2,name='nokia_4_2'),
    path('one_plus_7_pro/',views.one_plus_7_pro,name='one_plus_7_pro'),
    path('one_plus_7/',views.one_plus_7,name='one_plus_7'),
    path('oppo_reno_10x_zoom/',views.oppo_reno_10x_zoom,name='oppo_reno_10x_zoom'),
    path('realme3_pro/',views.realme3_pro,name='realme3_pro'),
    path('samsung_galaxy_a70/',views.samsung_galaxy_a70,name='samsung_galaxy_a70'),
    path('samsung_galaxy_s10e/',views.samsung_galaxy_s10e,name='samsung_galaxy_s10e'),
    path('xiaomi_redmi_k20_pro/',views.xiaomi_redmi_k20_pro,name='xiaomi_redmi_k20_pro'),
    path('xiaomi_redmi_k20/',views.xiaomi_redmi_k20,name='xiaomi_redmi_k20'),
    path('xiaomi_redmi_y3/',views.xiaomi_redmi_y3,name='xiaomi_redmi_y3'),
]

