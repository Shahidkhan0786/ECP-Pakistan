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
    path('', views.index),
    path('adminx/', views.adminnx),
    path('add/' , views.add_election,name="addelection"),
    path('addparty/' , views.add_party),
    path('addcandidate/' , views.add_Candidate),
    path('addseat/' , views.add_Seat),
    path('aboutecp/' ,views.about_ECP),
    path('aboutelections/' , views.about_Elections),
    path('parties/' , views.about_Parties),
    path('updates/', views.about_Updates),
    path('downloads/', views.Downloads ),
    path('contact/' ,views.contact_Us),
    path('regestration/' , views.voter_Registration),
    path('reg_form/' ,views.voter_reg_form ,name="reg_form"),
    path('castvote/' ,views.cast_Vote , name="castvote"),
    path('capture/' , views.capture ,name="capture"),
    path('open/' , views.camera_Open , name="open"),
    path('instructions/' ,views.show_Instructions , name="instructions"),
]
