
from django.urls import path,include
from . import views 
# from cureent dir import veiws

urlpatterns = [
    path('home',views.home),
    path('secondhome',views.secondhome)
    
]
