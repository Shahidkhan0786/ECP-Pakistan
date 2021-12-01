from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
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
    symbol_name=models.CharField(choices=SYMBOL_CHOICES,max_length=255)
    symbol_image=models.ImageField(null=True)

    def __str__(self):
        return self.symbol_name

class leader(models.Model):
    leader_Name= models.CharField(max_length=200)


    def __str__(self):
        return self.leader_Name


class constituency(models.Model):
    constituency=models.CharField(max_length=255)

    def __str__(self):
        return self.constituency

class seat(models.Model):
    seat_Name=models.CharField(max_length=255)
    constituency=models.ForeignKey(constituency ,on_delete=models.CASCADE)

    def __str__(self):
        return self.seat_Name
   

class Parties(models.Model):
    party_Name=models.CharField(max_length=200,choices=PARTY_NAME)
    party_Leader=models.ForeignKey(leader ,on_delete=models.CASCADE)
    party_Symbol=models.ForeignKey(symbol , on_delete=models.CASCADE)
    party_Overview=models.CharField(max_length=255)


    def __str__(self):
        return self.party_Name

class add_election(models.Model):
    election_type=models.CharField(max_length=100,choices=ELECTION_TYPE)
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)
    election_rules=models.CharField(max_length=255)

    def __str__(self):
        return self.election_type


class Candidate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party=models.OneToOneField(Parties ,on_delete=models.CASCADE)
    election=models.OneToOneField(add_election , on_delete=models.CASCADE)
    seat= models.ForeignKey(seat ,on_delete=models.CASCADE , null=True)
    image=models.FileField()

    def __str__(self):
        return self.user.username


class Voters(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    cnic=models.CharField(max_length=200)
    constituency=models.CharField(max_length=200)
    # constituency=models.ForeignKey(constituency , on_delete=models.CASCADE)
    dob=models.DateField()
    image=models.FileField()
    status=models.BooleanField(default=False ,null=True ,blank=True)

    def __str__(self):
        return self.user.username

