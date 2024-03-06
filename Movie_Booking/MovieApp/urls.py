from django.urls import path
from MovieApp import views
urlpatterns = [
    path('',views.login_fun,name='log'),
    path('reg',views.register_fun,name='reg'),
    path('home', views.home_fun, name='home'),
    path('add_movie',views.addmovie_fun,name='add_movie'),
    path('displaymovie',views.displaymovie_fun,name='displaymovie'),
    path('updatemovie/<int:movieid>',views.updatemovie_fun,name='updatemovie'),
    path('deletemovie/<int:movieid>',views.deletemovie_fun,name='deletemovie'),
    path('showtime',views.showtime_fun,name='showtime'),
    path('Booking',views.Booking_fun,name='Booking'),
    path('displayBooking',views.displayBooking_fun,name='displayBooking'),
    path('updateBooking/<int:movieid>',views.updateBooking_fun,name='updateBooking'),
    path('deleteBooking/<int:movieid>',views.deleteBooking_fun,name='deleteBooking'),
    path('logout',views.logout_fun,name='logout')
]
