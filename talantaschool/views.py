from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

from talantaschool.forms import LoginForm

# Create your views here.


# Create your views here.
def welcome(request):
    form=LoginForm()     
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data["email"]
            password=form.cleaned_data["password"]
            user=authenticate(email,password)
            
            if user is not None:
                login(request,user)    

                return redirect('student')

            else: 
             context = {'form': form,'message':'invalid Request'}
             return render(request, 'index.html', context)  



    context = {'form': form,}
    return render(request, 'index.html', context)

     


     
