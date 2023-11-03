
from django.urls import path,include
from . import views 
# from cureent dir import veiws

urlpatterns = [
    # path('hello/<str:name>',views.home),
    # path('about',views.about,name="about"),
    # path('contact',views.contact)
    # path('secondhome',views.secondhome)
    path('',views.index,name="homepage"),
    path('create',views.create,name="create"),
    path('delete/<int:id>',views.delete,name="deletepost"),
    path('signup', views.signup, name='signup'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),

     
    
]
