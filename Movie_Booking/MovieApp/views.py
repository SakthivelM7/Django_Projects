from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from MovieApp.models import Movie
from MovieApp.models import Hero,Heroin,Director,Theater,Showtime,Customer,Booking
from datetime import datetime

# Create your views here.
def login_fun(request):
    if request.method == "POST":
        user_name=request.POST['txtUsername']
        user_pwd=request.POST['txtPassword']
        u1=authenticate(username=user_name,password=user_pwd)

        if u1 is not None:
            if u1.is_superuser:#checking whrether data is superuser or not
                request.session['Uname']= user_name
                login(request,u1)
                return redirect('home')
        else:
            return render(request,'login.html',{'msg':'User name and password incorrect'})
    else:
        return render(request,'login.html')

def register_fun(request):
    if request.method == 'POST':
        first_name = request.POST['txtfirstname']
        last_name = request.POST['txtlastname']
        phno = request.POST['txtnum']
        email = request.POST['txtemail']
        password = request.POST['txtPassword']

        if User.objects.filter(username=first_name).exists():
            return render(request,'register.html', {'msg': 'Use proper username'})
        else:
            u1 = User.objects.create_superuser(username=first_name, last_name=last_name,phno=phno, email=email, password=password)
            u1.save()
            return redirect('log')
    else:
        return render(request, 'register.html')
@login_required
@never_cache
def home_fun(request):
    return render(request,'adminhome.html',{'data':request.session['Uname']})

def addmovie_fun(request):
    if request.method =='POST':
        c1=Movie()
        c1.mov_id = request.POST['txtmovid']
        c1.mov_name=request.POST['txtmovName']
        c1.hero_name=Hero.objects.get(hero_name=request.POST['ddlhero'])
        c1.heroin_name=Heroin.objects.get(heroin_name=request.POST['ddlheroin'])
        c1.director_name=Director.objects.get(director_name=request.POST['ddldirector'])
        c1.cost=int(request.POST['txtcost'])
        c1.save()
        return redirect('add_movie')
    else:
        hero = Hero.objects.all()
        heroin = Heroin.objects.all()
        director = Director.objects.all()
        return render(request, 'addmovie.html', {'herodata': hero, 'heroindata': heroin,'directordata':director})
@login_required
@never_cache
def displaymovie_fun(request):
    c1 = Movie.objects.all()
    return render(request, 'displaymovie.html', {'moviedata': c1})
@login_required
@never_cache
def updatemovie_fun(request,movieid):
    c1=Movie.objects.get(id=movieid)
    if request.method=='POST':
        c1.mov_id = request.POST['txtmovid']
        c1.mov_name = request.POST['txtmovName']
        c1.hero_name = Hero.objects.get(hero_name=request.POST['ddlhero'])
        c1.heroin_name = Heroin.objects.get(heroin_name=request.POST['ddlheroin'])
        c1.director_name = Director.objects.get(director_name=request.POST['ddldirector'])
        c1.cost = int(request.POST['txtcost'])
        c1.save()
        return redirect('displaymovie')
    else:
        hero = Hero.objects.all()
        heroin = Heroin.objects.all()
        director = Director.objects.all()
        return render(request, 'upadatemovie.html', {'movie': c1,'herodata': hero, 'heroindata': heroin, 'directordata': director})
@login_required
@never_cache
def deletemovie_fun(request,movieid):
    c1=Movie.objects.get(id=movieid)
    c1.delete()
    return redirect('displaymovie')
@login_required
@never_cache
def showtime_fun(request):
    if request.method =='POST':
        c1=Showtime()
        c1.mov_id=Movie.objects.get(mov_name=request.POST['ddlmovie'])
        c1.theater_name = Theater.objects.get(theater_name=request.POST['ddltheater'])
        date_str = request.POST['txtdate']
        c1.datetime = datetime.strptime(date_str, '%d %B %Y')  # Adjust the format based on your form input
        c1.save()
        return redirect('showtime')
    else:
        mov_id = Movie.objects.all()
        theater_name = Theater.objects.all()
        return render(request, 'showtime.html', {'moviedata': mov_id, 'theaterdata':theater_name})
@login_required
@never_cache
def Booking_fun(request):
    if request.method =='POST':
        c1=Booking()
        c1.mov_id=Movie.objects.get(mov_name=request.POST['ddlmovie'])
        c1.cust_id = Customer.objects.get(Fname=request.POST['ddlcust'])
        c1.No_of_seats=int(request.POST['txtseats'])

        m1 = Movie.objects.get(mov_name=request.POST['ddlmovie'])
        # c1.cost = int(request.POST['txtcost'])
        c1.cost= c1.No_of_seats * m1.cost
        c1.save()
        return redirect('Booking')
    else:
        mov_id = Movie.objects.all()
        cust_id = Customer.objects.all()
        return render(request, 'Booking.html', {'moviedata': mov_id, 'custdata':cust_id })
@login_required
@never_cache
def displayBooking_fun(request):
    c1 = Booking.objects.all()
    return render(request, 'displayBooking.html', {'Bookingdata': c1})
@login_required
@never_cache
def updateBooking_fun(request,movieid):
    c1 = Booking.objects.get(id=movieid)
    if request.method == 'POST':
        c1.mov_id = Movie.objects.get(id=request.POST['ddlmovie'])
        c1.cust_id = Customer.objects.get(id=request.POST['ddlcust'])
        c1.No_of_seats = request.POST['txtseats']
        if No_of_seats>1:
            c1.cost = c1.No_of_seats * m1.cost
        c1.save()
        return redirect('displayBooking')
    else:
        mov_id = Booking.objects.all()
        cust_id = Booking.objects.all()
        return render(request, 'upadateBooking.html', {'Booking': c1, 'moviedata': mov_id, 'custdata': cust_id})
@login_required
@never_cache
def deleteBooking_fun(request,movieid):
    c1=Booking.objects.get(id=movieid)
    c1.delete()
    return redirect('displayBooking')

def logout_fun(request):
    logout(request)
    del request.session['Uname']
    return redirect('log')
