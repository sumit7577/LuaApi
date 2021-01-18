from django.shortcuts import render,HttpResponse
from .models import Customer
from django.views.decorators.csrf import  csrf_protect
from datetime import date
# Create your views here.
@csrf_protect
def home(request):
	if request.method =="POST":
		name = request.GET.get("test1")
		email = request.GET.get("test2")
		device = request.GET.get("test3")
		
		user = Customer.objects.filter(name=name,password=email,device=device,timestamp__gt=date.today()).all()
		dataCheck = user.count()
		print(dataCheck)
		if dataCheck == True:
			return render(request,"/shop/highlyencrypt.txt")
		else:
			return  HttpResponse("Bad")
	return render(request,"shop/index.html")
	