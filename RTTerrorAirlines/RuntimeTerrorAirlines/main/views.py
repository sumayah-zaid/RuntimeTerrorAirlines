from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt  

def index(request):
    return redirect('/search_flights')

def signup(request):
    return render(request, 'signup.html')

def signup_process(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/signup')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        bdate = request.POST['birth-date']
        phone = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        pwd_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode() # create the hash
        user = User.objects.create(first_name=fname, last_name=lname, birth_date=bdate, phone_number=phone, email=email, password=pwd_hash)
        request.session['logged_in'] = user.id 
        return redirect('/dashboard')

def login(request):
    return render(request, 'login.html')

def login_process(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, val in errors.items():
            messages.error(request, val)
        return redirect('/login')
    else:
        user = User.objects.get(email=request.POST['email'])
        if user.isAdmin:
            request.session['logged_in'] = user.id
            return redirect('/admin/dashboard')
        else:    
            request.session['logged_in'] = user.id 
            return redirect('/dashboard')


def admin_dashboard(request):
    context = {
        "all_flights" : Flight.objects.all().order_by("-id"),
    }
    return render(request, 'AdminDashboard.html', context)


def admin_add_flight(request):
    return render(request, 'AddFlight.html')

def new_flight(request):
    airline = request.POST['airline']
    from_city = request.POST['fcity']
    to_city = request.POST['tcity']
    from_airport = request.POST['fair']
    to_airport = request.POST['toair']
    departure_date = request.POST['dep']
    departure_time = request.POST['deptime']
    landing_date = request.POST['landate']
    landing_time = request.POST['lantime']
    flight_duration = request.POST['fldep']
    economy_price = request.POST['ecprice']
    business_price = request.POST['busprice']
    number_of_stops = request.POST['numstop']
    waiting_time = request.POST['waitime']

    flight = Flight.objects.create(airline = airline, from_city=from_city, to_city=to_city, from_airport=from_airport, to_airport=to_airport, departure_time=departure_time, landing_time=landing_time, flight_duration=flight_duration, economy_price=economy_price, business_price=business_price, number_of_stops=number_of_stops, waiting_time=waiting_time, departure_date=departure_date, landing_date=landing_date)

    return redirect("/admin/dashboard")



def admin_edit_flight(request, id):
    context = {
        "flight" : Flight.objects.get(id=id)
    }
    return render(request, 'EditFlight.html', context)


def admin_update_flight(request, id):
    airline = request.POST['airline']
    from_city = request.POST['fcity']
    to_city = request.POST['tcity']
    from_airport = request.POST['fair']
    to_airport = request.POST['toair']
    departure_date = request.POST['dep']
    departure_time = request.POST['deptime']
    landing_date = request.POST['landate']
    landing_time = request.POST['lantime']
    flight_duration = request.POST['fldep']
    economy_price = request.POST['ecprice']
    business_price = request.POST['busprice']
    number_of_stops = request.POST['numstop']
    waiting_time = request.POST['waitime']

    flight = Flight.objects.get(id=id)

    flight.airline = airline 
    flight.from_city=from_city
    flight.to_city=to_city
    flight.from_airport=from_airport
    flight.to_airport=to_airport
    flight.departure_time=departure_time
    flight.landing_time=landing_time
    flight.flight_duration=flight_duration
    flight.economy_price=economy_price
    flight.business_price=business_price
    flight.number_of_stops=number_of_stops
    flight.waiting_time=waiting_time
    flight.departure_date=departure_date
    flight.landing_date=landing_date
    flight.save()
    return redirect("/admin/dashboard")



def admin_delete_flight(request, id):
    flight = Flight.objects.get(id=id)
    flight.delete()
    return redirect('/admin/dashboard')

def user_search(request):
    return render(request, 'home.html')

# def search_results(request):
#     return render(request, 'search_results.html')

def user_dashboard(request):
    if request.session is None:
        return redirect("/login")
    else:
        user_bookings = Flight.objects.filter(on_flight = request.session['logged_in'])
    context = {
        "user_bookings" : user_bookings,
        "logged_in" : User.objects.get(id=request.session['logged_in']),
    }
    return render(request, 'UserDashboard.html', context)

def book_flight_depart(request):

    depart_country = request.POST['depart_country']
    land_country = request.POST['land_country']
    depart_date = request.POST['depart_date']
    passengers = request.POST['adult_counter']

    request.session['passengers'] = passengers;

    flight = Flight.objects.filter(from_city=depart_country).filter(to_city=land_country).filter(departure_date=depart_date)

    context = {
        "passengers": passengers,
        "depart_date":depart_date,
        "flights": flight,
    }

    return render(request, 'flight_selection_departure.html', context)



# def book_flight_return(request):
#     return render(request, 'flight_selection_return.html')

# def book_flight_passenger(request):
#     total_price = request.POST['total_price'];
#     context = {
#         "total_price":total_price,
#     }
#     return render(request, 'passenger.html', context)

def payment(request, id):
    total_price = request.POST['total_price'];
    context = {
        "id" : id,
        "total_price":total_price,
    }
    return render(request, 'payment.html',context)

def book_flight(request, id):
    flight = Flight.objects.get(id=id)
    user = User.objects.get(id=request.session['logged_in'])
    flight.on_flight.add(user)
    return redirect("/dashboard")

def logout(request):
    request.session.flush()
    return redirect("/login")