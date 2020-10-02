from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib import messages
from demoapp1.models import Account
# Create your views here.
def  index(request):
	print(request.POST.get('name'))

	if request.method == 'POST':
		have_name = Account.objects.filter(username=request.POST.get('name')).exists()
		have_password = Account.objects.filter(password=request.POST.get('password')).exists()
		if have_name == False:
			messages.info(request,"username not exist")
			
		if have_name == False:
			messages.info(request,"wrong password")
		if have_name == True and have_password == True:
			request.session['username'] = request.POST.get('name')
			return HttpResponseRedirect('/')
	return render(request,'login.html')

def mainpage(request):
	if 'username' not in request.session:
		return HttpResponseRedirect('/login')
	if (request.POST.get('logout')):
		del request.session['username']
		return HttpResponseRedirect('/login')
	
	return render(request,'test.html',{'username':request.session['username']})


def create(request):
	if request.method == 'POST':
		if request.POST.get('name') == '' or request.POST.get('password1') == '' or request.POST.get('password2') == '':
			messages.info(request,"Enter missing information")
		else:
			print("here")
			check= password_check(request.POST.get('password1'),request.POST.get('password2'))
			if check == True:
				new = Account()
				new.username = request.POST.get('name')
				new.password = request.POST.get('password1')
				new.save()
				return HttpResponseRedirect('/login')
	return render(request,'create.html')

def password_check(p1,p2):
	if p1 == p2:
		return True
	else:
		return False

	