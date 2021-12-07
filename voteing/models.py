from datetime import date, datetime
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User, update_last_login
from django.http import request
# Create your models here.

SYMBOL_CHOICES=(
    ("BALA" ,"BALA"),
    ("LOTA" , "LOTA"),
    ("SHAR" ,"SHAR"),
    ("TEAR" ,"TEAR"),
)

PARTY_NAME=(
    ("Pakistan Tehreek-e-Insaf" ,"Pakistan Tehreek-e-Insaf"),
    ("Pakistan Muslim League (N)","Pakistan Muslim League (N)"),
    ("Pakistan Muslim League","Pakistan Muslim League"),
    ("Pakistan Peoples Party","Pakistan Peoples Party"),
    ("Jamaat-e-Islami","Jamaat-e-Islami"),
)

ELECTION_TYPE=(
    ("general" ,"general"),
    ("local" , "local"),
)


class symbol(models.Model):
    symbolName=models.CharField(choices=SYMBOL_CHOICES,max_length=255 ,unique=True)
    symbolImage=models.ImageField(upload_to='symbols/',null=True)

    def __str__(self):
        return self.symbolName

class leader(models.Model):
    leaderName= models.CharField(max_length=200 ,unique=True)


    def __str__(self):
        return self.leaderName


class constituency(models.Model):
    constituency=models.CharField(max_length=255 ,unique=True)

    def __str__(self):
        return self.constituency

class seat(models.Model):
    seatName=models.CharField(max_length=255 ,unique=True)


    def __str__(self):
        return self.seatName
   

class Parties(models.Model):
    partyName=models.CharField(max_length=200,choices=PARTY_NAME , unique=True)
    partyLeader=models.ForeignKey(leader ,on_delete=models.CASCADE)
    partySymbol=models.ForeignKey(symbol , on_delete=models.CASCADE)
    partyOverview=models.CharField(max_length=255)


    def __str__(self):
        return self.partyName

class add_election(models.Model):
    electiontype=models.CharField(max_length=100,choices=ELECTION_TYPE)
    startdate=models.DateTimeField(null=True)
    enddate=models.DateTimeField(null=True)
    electionrules=models.CharField(max_length=255)

    def __str__(self):
        return self.electiontype


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party=models.OneToOneField(Parties ,on_delete=models.CASCADE)
    election=models.ForeignKey(add_election ,on_delete=models.CASCADE , null=True)
    
    seat= models.ForeignKey(seat ,on_delete=models.CASCADE , null=True)
    image=models.FileField(upload_to="candidate")

    def __str__(self):
        return self.user.username


class Voters(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    cnic=models.CharField(max_length=200 , unique=True)
    constituency=models.CharField(max_length=200)
    # constituency=models.ForeignKey(constituency , on_delete=models.CASCADE)
    dob=models.DateField()
    image=models.FileField(upload_to="voter/")
    status=models.BooleanField(default=False ,null=True ,blank=True)

    def __str__(self):
        return self.user.username


class news(models.Model):
    author=models.ForeignKey(User , on_delete=models.CASCADE)
    datetime=models.DateTimeField(auto_now_add=True , null=True)
    title=models.CharField(max_length=255)
    content=models.TextField()
    image=models.FileField(upload_to='news/')
    
    def __str__(self):
        return self.title




class ElectionReslts(models.Model):
    vuser=models.CharField(max_length=255 , unique=True)
    Candidate=models.CharField(max_length=255)
    party=models.CharField(max_length=255)
    seat=models.CharField(max_length=255)





