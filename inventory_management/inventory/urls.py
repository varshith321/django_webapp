from django.conf.urls import url
from .views import *

urlpatterns = [
    #url(r'^$', index, name='index'),
    url(r'^$', index, name='calendar'),
    url(r'^resturant$', display_resturant, name="display_resturant")
    

]