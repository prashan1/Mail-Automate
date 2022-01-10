from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver 
from .weather_api import SendingClass
from collections import defaultdict
from django.utils import timezone

# Limited choices of cities
choices = ( ("Mumbai","Mumbai"), ("Delhi", "Delhi"),("Chennai", "Chennai"), ("Bangalore","Bangalore"),("Kolkata", "Kolkata"))
# Creating model for receiver data
class Send_Email(models.Model):
    
    Name = models.CharField(max_length = 100 , blank=False )
    email = models.EmailField(blank=False )
    recipient_city = models.CharField( max_length = 100 , choices=choices,blank=False)
    sending_time = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.Name 

# Using Signals to send an email whenever receiver's data is saved in database
@receiver(post_save, sender=Send_Email)
def send_email(sender, instance, created, **kwargs):

    # SendingClass in weather_api module is use to build complete logic of sending email to receiver ends
    sending = SendingClass(instance.Name, instance.email , instance.recipient_city)
    sending.sendEmail()

