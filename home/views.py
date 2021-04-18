from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import Group,User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,authenticate

def home(request,table_num):
	request.session['table_num'] = table_num
	return render(request,'home/home.html')

def main(request):
	bev=Bevereges.objects.all()
	bir=Birthday.objects.all()
	swe=Sweets.objects.all()
	comb=Combos.objects.all()
	bur=Burger.objects.all()
	com=Combo.objects.all()
	chi=Chinese.objects.all()
	par=Paratha.objects.all()
	ice=Icecream.objects.all()
	ric=rice.objects.all()
	rol=rolls.objects.all()
	san=sandwitch.objects.all()
	sna=Snacks.objects.all()
	sou=SouthIndian.objects.all()
	tha=Thali.objects.all()

	context={
	'bir':bir,
	'swe':swe,
	'comb':comb,
	'bev':bev,
	'bur':bur,
	'com':com,
	'chi':chi,
	'par':par,
	'ice':ice,
	'ric':ric,
	'rol':rol,
	'san':san,
	'sna':sna,
	'sou':sou,
	'tha':tha
	}

	return render(request,'home/main.html',context)

def signupView(request):
	if request.method=='POST':
		form=SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username=form.cleaned_data.get('username')
			signup_user=User.objects.get(username=username,)
			customer_group=Group.objects.get(name='Customer')
			customer_group.user_set.add(signup_user)
	else:
		form=SignUpForm()

	return render(request,'accounts/signup.html',{'form':form})


def signinView(request):
	if request.method=='POST':
		form=AuthenticationForm(data=request.POST)
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			bev=Bevereges.objects.all()
			bur=Burger.objects.all()
			com=Combo.objects.all()
			chi=Chinese.objects.all()
			par=Paratha.objects.all()
			ice=Icecream.objects.all()
			ric=rice.objects.all()
			rol=rolls.objects.all()
			san=sandwitch.objects.all()
			sna=Snacks.objects.all()
			sou=SouthIndian.objects.all()
			tha=Thali.objects.all()

			context={
				'bev':bev,
				'bur':bur,
				'com':com,
				'chi':chi,
				'par':par,
				'ice':ice,
				'ric':ric,
				'rol':rol,
				'san':san,
				'sna':sna,
				'sou':sou,
				'tha':tha
			}

			return render(request,'home/main.html',context)
		else:
			return redirect('/register')
	else: 
		form=AuthenticationForm()
	return render(request,'accounts/signin.html',{'form':form})



	
