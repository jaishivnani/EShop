from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.product import Product
from .models.category import Category
from .models.customer import Customer

# Create your views here.


def index(request):
     products = None
     categories = Category.get_all_categories()
     categoryID = request.GET.get('category')
     if categoryID:
          products = Product.get_all_products_by_categoryid(categoryID)
     else:
          products = Product.get_all_products()

     data = {}
     data['products'] = products
     data['categories'] = categories
     
     return render(request,'index.html',data)

def signup(request):
     if request.method == 'GET':
          return render(request, 'signup.html')    
     else:
          postData = request.POST
          first_name = postData.get('firstname')
          last_name = postData.get('lastname')
          phone = postData.get('phone')
          email = postData.get('email')
          password = postData.get('password')
          #Validation
          error_message = None
          if not first_name:
               error_message="First Name Required!!"
          elif len(first_name)<3:
               error_message="First Name must be 3 characters long"
          elif not last_name:
               error_message="Last Name Required!!"
          elif len(last_name)<3:
               error_message="Last Name must be 3 characters long"
          elif not phone:
               error_message = "Phone Number Required!!"
          elif len(phone) < 10:
               error_message = "Phone Number must be 10 char Long"
          elif not password:
               error_message = "Please enter a password"
          elif len(password)<6:
               error_message = "Password must be 6 char long"
          elif len(password)>15:
               error_message = "Password must not be greater than 15 characters"
          elif not email:
               error_message = "Please enter an email"
          elif len(email)<5:
               error_message = "Email must be 5 char long"

          #saving
          if not error_message:
               print(first_name,last_name,phone,email,password)
               customer = Customer(first_name=first_name,last_name=last_name,phone=phone,email=email,password=password)
               customer.register()
          else:
               return render(request,'signup.html',{'error':error_message})