from django.db import models
from django.contrib.auth.models import User

import games
 
class SportsSession(models.Model):
    name = models.CharField('Session Name', max_length=20, default="Session")
    date = models.DateTimeField('Session Date')
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

class Section(models.Model):
    start_time = models.TimeField('Start Time')
    end_time = models.TimeField('End Time')
    sports_session = models.ForeignKey(SportsSession, on_delete=models.CASCADE, null=True, related_name="section")
    game = models.OneToOneField(games.models.Game, on_delete=models.CASCADE, null=True)
    


    
    
    
    