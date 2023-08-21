from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User,auth
from globaldata.models import Contact
from .forms import signupform, contactform



def home(request):
    return render(request, "home.html")



@csrf_exempt
def register(request):
    form=signupform()
    if request.method == 'POST':
        form = signupform(request.POST)
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        first_name= request.POST['first_name']
        email = request.POST['email']

        if(password1==password2):
            if(User.objects.filter(username=username).exists()):
                message='Username taken'
                return render(request, 'signup.html', {'form': form})
            if(User.objects.filter(first_name=first_name).exists()):
                message='Phone Number already registered'
                return render(request, 'signup.html', {'form': form})
            elif User.objects.filter(email=email).exists():
                message = 'Email already registered'
                return render(request, 'signup.html', {'form': form})
            else:
                user = User.objects.create(username=username, email=email,first_name=first_name)
                user.set_password(password1)
                user.save()
                return redirect('login')
    return render(request, "signup.html",{'form':form})



@csrf_exempt
def Login(request):
    message=''
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # login(request,user)
            auth.login(request, user)
            return redirect('home')
        else:
            message="invalid credentials"
    return render(request, 'login.html', {'message':message})




def addcontact(request):
    message=''
    if(request.method=='POST'):
        form = contactform(request.POST)
        # if form.is_valid():
        name = request.POST['name']
        phone_number = request.POST['phone_number']
        isspam = request.POST['isspam']
        try:
            contact = Contact.objects.get(phone_number=phone_number)
            if(isspam=='2'):
                contact.spam_count = contact.spam_count +1
                contact.save()  
        except Contact.DoesNotExist:
            if(isspam=='2'):
                count=1
            else:
                count=0
            contact = Contact.objects.create(name=name, phone_number=phone_number,spam_count=count)
            contact.save()
        message='thank you'
    fm=contactform()
    return render(request, 'addcontact.html', {'fm': fm, 'm':message})




def search(request):
    return render(request, 'search.html')



def searchbyname(request):
    di={}
    message=''

    if request.method == 'POST':
        name = request.POST['name']

        try:
            contact = Contact.objects.get(name = name)
            di = {
                'name' : contact.name,
                'number' : contact.phone_number,
                'likelihood': f'{contact.spam_count} people marked it as spam',
            }
        except Contact.DoesNotExist:
            message = "no record found"
    
    return render(request, 'searchbyname.html', {'m':message, 'di':di})



def searchbyphone(request):
    message=''
    di={}
    if request.method == 'POST':
        phone_number = request.POST['phone_number']

        try:
            contact = Contact.objects.get(phone_number=phone_number)
            di = {
                'name' : contact.name,
                'number' : contact.phone_number,
                'likelihood': f'{contact.spam_count} people marked it as spam',
            }
        except Contact.DoesNotExist:
            message = "no record found"
    
    return render(request, 'searchbyphone.html', {'m':message, 'di':di})

