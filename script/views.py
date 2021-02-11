from django.shortcuts import render,HttpResponse
from .models import Customer
from django.views.decorators.csrf import  csrf_protect
from datetime import date
# Create your views here.
@csrf_protect
def home(request):
	if request.method =="GET":
		name = request.GET.get("test1")
		email = request.GET.get("test2")
		device = request.GET.get("test3")
		script = request.GET.get("name")
		
		user = Customer.objects.filter(name=name,password=email,deviceIMEI=device,expiryDate__gt=date.today(),scriptName=script).all()
		dataCheck = user.count()
		print(dataCheck)
		if dataCheck == True:
		    return render(request,f"shop/{script}")
		else:
			return HttpResponse("gg.prompt(Are u krezy)")
	return render(request,"shop/index.html")
	