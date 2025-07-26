from django.shortcuts import render, redirect

# Create your views here.
def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Contact(request):
    return render(request, 'contact.html')

def A(request):
    return render(request, 'A.html')


def Img(request):
    return render(request, 'Img.html')

# Hardcoded credentials
USERNAME = 'Sharad'
PASSWORD = 'Love143'
def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username == USERNAME and password == PASSWORD:
            request.session['logged_in'] = True
            return redirect('home')
        else:
            # Only send error on failed POST
            return render(request, 'login.html', {
                'error': 'Hey you cannot login, Only my Motuuu can open this!!!'
            })

    # No error shown on first GET request
    return render(request, 'login.html')

def Home(request):
    if not request.session.get('logged_in'):
        return redirect('login')
    return render(request, 'home.html')  

def Logout(request):
    request.session.flush()
    return redirect('login')
