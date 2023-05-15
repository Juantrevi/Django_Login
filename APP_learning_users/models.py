from django.db import models
from django.contrib.auth.models import User

#Create your model here. (Although there are some features already created)
#With the base User model we already have:
# - User name
# - Email
# - Password
# - First name
# - Last name
# If we want our user to have more fields we use this next class

class UserProfileInfo(models.Model):

    #Create relationship (Don't inherit from User!)
    #This means this extra user profile info, has a direct one to one conection to the User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #Add any additional attributes you want
    portfolio = models.URLField(blank=True) #No error if they dont provide a portfolio
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):

        return self.user.email




