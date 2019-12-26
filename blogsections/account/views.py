from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render

#from blogsections.account.forms import LoginForm
import pyrebase

config = {
    'apiKey': "AIzaSyBndwG3xeoZ_xiecS1AHlXNQCHWdXU4eXE",
    'authDomain': "epicturkey-6abfa.firebaseapp.com",
    'databaseURL': "https://epicturkey-6abfa.firebaseio.com",
    'projectId': "epicturkey-6abfa",
    'storageBucket': "epicturkey-6abfa.appspot.com",
    'messagingSenderId': "543046502770",
    'appId': "1:543046502770:web:3d69be495e5315804db5eb",
    'measurementId': "G-VB5FT6KYR6"
  }

firebase = pyrebase.initialize_app(config)

authe = firebase.auth()
database=firebase.database()

def singIn(request):

    return render(request, "registration/login.html")


def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"registration/login.html",{"msg":message})
    print(user)
    return render(request, "app/home.html",{"e":email})

def signUp(request):

    return render(request,"registration/register.html")
def postsignup(request):

    name=request.POST.get('name')
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    try:
        user=authe.create_user_with_email_and_password(email,passw)
        uid = user['localId']
        data={"name":name,"status":"1"}
        database.child("users").child(uid).child("details").set(data)
    except:
        message="Unable to create account try again"
        return render(request,"registration/register.html",{"messg":message})



    return render(request,"registration/login.html")
"""
class LoginView(LoginView):
    form_class = LoginForm
    template_name= 'registration/login.html'
"""
def logout(request):
    authe.logout(request)
    return render(request,'signIn.html')

class LogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
