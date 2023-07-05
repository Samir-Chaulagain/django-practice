
from django.urls import path,include
from . import views 
# from cureent dir import veiws

urlpatterns = [
    path('hello/<str:name>',views.home),
    path('about',views.about,name="about"),
    path('contact',views.contact)
    # path('secondhome',views.secondhome)
    
]
