"""ECP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name="home"),
    path('admin/', views.adminnx ,name="aadmin"),
    path('admindash/', views.admin_Dash ,name="admindash"),
    path('logout/' ,views.adminlogout , name="adminlogout"),
    path('add/' , views.add_election,name="addelection"),
    path('addparty/' , views.add_party , name="addparty"),
    path('addpartyleader/' , views.addpartyleader , name="addpartyleader"),
    path('addpartysymbol/' , views.addpartysymbol , name="addpartysymbol"),
    path('addcandidate/' , views.add_Candidate , name="addcandidate"),
    path('addseat/' , views.add_Seat , name='addseat'),
    path('aboutecp/' ,views.about_ECP),
    path('aboutelections/' , views.about_Elections),
    path('parties/' , views.about_Parties),
    path('updates/', views.about_Updates),
    path('downloads/', views.Downloads ),
    path('contact/' ,views.contact_Us),
    path('regestration/' , views.voter_Registration),
    path('reg_form/' ,views.voter_reg_form ,name="reg_form"),
    path('castvote/' ,views.cast_Vote , name="castvote"),
    path('capture/<int:id>/' , views.capture ,name="capture"),
    path('open/' , views.camera_Open , name="open"),
    path('instructions/' ,views.show_Instructions , name="instructions"),
    path('homourecp/' , views.honourable__ecp , name="honourableecp"),
    path('ballet/' , views.ballet , name="ballet"),

    path('electionresult/' , views.electionResult , name="electionresult"),
    path('checkcnic/<int:cid>/' , views.checkCnic , name="cniccheck"),
    path('listof/' , views.partiesList , name="partieslist"),
    path('listofsymbol/' , views.symbolList , name="symbollist"),
    path('listofcandidate/' , views.candidateList , name="candidatelist"),
    path('checkreg/' , views.checkRegestration , name="ckeckreg"),
    # //admin
    path('chk_reg' , views.check_voter_reg , name="checkvoterreg"),
    path('show-res',views.results, name="show-results"),
    path('news/' , views.addNews , name='addnews'),
   
]
