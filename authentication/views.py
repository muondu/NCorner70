from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
def home(request):
    return render(request, "authentication/index.html")

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        

        myuser = User.objects.create_user(username, email, pass1,)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your account has been generated")
        return redirect('signin')


    return render(request, "authentication/signup.html")



def signin(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        
        if username =="dmuondu" and pass1 == "apple12.":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/danielStatement.html")

        elif username =="trotich" and pass1 == "mercury452!":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/timothystatement.html")

        elif username =="hkyalo" and pass1 == "venus84#":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/henrystatement.html")
        elif username =="pthuku" and pass1 == "earth12>":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/peterstatement.html")
            
        elif username =="patwachira" and pass1 == "mars12345":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/patricstatement.html")
        
        elif username =="bmwaura" and pass1 == "jupiter12^":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/benstatement.html")
        elif username =="aojwang" and pass1 == "saturn12&":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/anderewstatement.html")
        elif username =="dnjogu" and pass1 == "neptune12*":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/Duncanstatement.html")

        elif username =="erigha" and pass1 == "sun12345(":
            login(request, user)
            fname = user.first_name
            return render(request, "authentication/users/Edwinstatement.html")
        
        
        else:
            messages.error(request, "Wrong credidentials")
            return redirect('home')

    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('home')