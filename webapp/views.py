from django.shortcuts import render, redirect
from products.models import Product
from webapp.forms import ContactUsForm


# Create your views here.
def home(request):
    products = Product.objects.filter(is_new_arrival = True)

    return render(request,'home.html',{'products':products})

def why_us(request):
    return render(request,'why.html')

def testimonial(request):
    return render(request,'testimonial.html')

def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contactus')
    else:
        form = ContactUsForm()
        
    return render(request,'contact.html',{'form':form})

def shop(request):
    products = Product.objects.all().order_by('-is_new_arrival')
    return render(request,'shop.html',{'products': products})
