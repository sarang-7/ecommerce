from django.contrib import admin
from django.urls import path
from webapp.views import home,why_us,testimonial,contactus,shop


urlpatterns = [
    path('',home,name="home" ),
    path('whyus',why_us,name="why_us" ),
    path('testimonial',testimonial,name="testimonial"),
    path('contactus/',contactus,name="contactus" ),
    path('shop',shop,name="shop" ),


] 

