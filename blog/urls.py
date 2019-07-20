from django.urls import path

from blog.views import listele, goruntule,myview

urlpatterns = [
    path('', listele,),
    path('gonderi/<int:gonderi_id>/', goruntule),
    path('myview',myview),
]

