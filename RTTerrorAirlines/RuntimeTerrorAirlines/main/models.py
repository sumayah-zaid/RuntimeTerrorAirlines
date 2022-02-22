from django.db import models
import re, datetime
import bcrypt 

# Create Model Manger 
class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        user_in_db = User.objects.filter(email=postData['email'])
        if len(postData['fname']) < 2:
            errors['fname'] = "Your first name need to have more than 2 characters"
        if len(postData['lname']) < 4:
            errors['lname'] = "Your last name need to have more than 4 characters"
        if len(postData['birth-date']) < 1:
            errors['birth-date'] = "Your Birth date must be provided!"
        elif postData['birth-date']:
            birth_date = datetime.datetime.strptime(postData['birth-date'], "%Y-%m-%d")
            if datetime.datetime.today() < birth_date:
                    errors['birth-date'] = "Your birth date must be in the past!"
        if len(postData['phone_number']) < 10:
            errors['phone_number'] = "Your phone number need to have 10 numbers!"      
        if len(postData['password']) < 8:
            errors['password'] = "Your password need to have more than 8 characters!"
        if postData['password'] != postData['pwd_confirm']:
            errors['password'] = "Passwords must match!"
        if user_in_db:
            errors['email'] = "User already exists"
        return errors 
    
    def login_validator(self, postData ):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            login_user = user[0]
            if not bcrypt.checkpw(postData['password'].encode(), login_user.password.encode()):
                errors['password'] = "Invalid login!"
        else:
            errors['password'] = "Invalid login!"
        return errors 




# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    phone_number = models.PositiveIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=15)
    isAdmin = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Flight(models.Model):
    airline = models.CharField(max_length=50)
    from_city = models.CharField(max_length=15)
    to_city = models.CharField(max_length=15)
    from_airport = models.CharField(max_length=50)
    to_airport = models.CharField(max_length=50)
    departure_date = models.DateField()
    departure_time = models.TimeField()
    landing_date = models.DateField()
    landing_time = models.TimeField()
    flight_duration = models.CharField(max_length=15)
    economy_price = models.CharField(max_length=15)
    business_price = models.CharField(max_length=15)
    number_of_stops = models.IntegerField()
    waiting_time = models.CharField(max_length=15)

    on_flight = models.ManyToManyField(User, related_name="flight")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
