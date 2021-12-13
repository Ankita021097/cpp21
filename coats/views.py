from django.shortcuts import render
from .models import Product,Orders

# Create your views here.
 
def index(request):
  product_objects = Product.objects.all()
  
  #Search code
  
  item_name = request.GET.get('item_name')
  if item_name != '' and item_name is not None:
    product_objects = product_objects.filter(title__icontains = item_name)
  return render(request,'coats/index.html',{'product_objects':product_objects})
 
def detail (request,id):
    product_object = Product.objects.get(id=id)
    return render(request,'coats/detail.html',{'product_object':product_object})
    
    
def checkout(request):
  
      if request.method == "POST":
        items = request.POST.get('items',"")
        name = request.POST.get('name',"")
        email = request.POST.get('email',"")
        address = request.POST.get('address',"")
        city = request.POST.get('city',"")
        state =request.POST.get('state',"")
        zipcode = request.POST.get('zipcode',"")
        
        order = Orders(items=items,name=name,email=email,address=address,city=city,state=state,zipcode=zipcode)
        order.save()
        
        print('1234')
        
      return render(request,'coats/checkout.html')
    