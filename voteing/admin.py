from django.contrib import admin
from .models import Updates, seat,add_election,Parties,leader,symbol,Candidate,constituency,Voters,news ,ElectionReslts,Updates,Contact,download
# Register your models here.

admin.site.register(ElectionReslts)
admin.site.register(symbol)
admin.site.register(leader)
admin.site.register(seat)
admin.site.register(add_election)
admin.site.register(Parties)
admin.site.register(Candidate)
admin.site.register(constituency)
admin.site.register(Voters)
admin.site.register(news)
admin.site.register(Updates)
admin.site.register(Contact)
admin.site.register(download)