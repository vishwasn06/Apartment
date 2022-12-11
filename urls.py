"""Apartment URL Configuration

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


from typing import NewType
from hotel.views import checkavil, guestcheckfacility, homepage
from django.contrib import admin
from django.contrib import auth
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from myapp.views import (
 #   BookingListView,
 #   BookingView,
 #   CancelBookingView,
    allbill_detail_view,
    allemergency_detail_view,
    #allreport,
    bill_detail_view,
    buy_view,
    checkfacility_view,
#    change_room_view,
    contact_detail_view,
    emergency_detail_view,
   # RoomList,
    home_screen_view,
    report_detail_view, 
   # room_detail_view,
#    booking_detail_view,
    guest_screen_view,
    guest_screen,
    emergency_detail,
 #   RoomListView,
   # buy_screen_view,
    rept_view,
)
from django.contrib.auth import views as auth_views
from notification.views import notifications
from account.views import (
    account_view,
    guest_register,
  
    newprofile,
    profile,
    resident_register, 
    login_request, 
    register,
    logout_view,
   

)
admin.site.site_header = 'Apartment Admin'
admin.site.site_title = 'Apartment Admin'
admin.site.site_url = 'http://Apartment.com/'
admin.site.index_title = 'Apartment administration'
admin.empty_value_display = '**Empty**'
import hotel.views as views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('myapp.urls')),
    path('home4/', views.homepage,name="homepage"),
    path('', home_screen_view, name="home"),
    path('home3/', homepage, name="home3"),
  
    path('register/', register, name="register"),
    path('logout/', logout_view, name="logout"),
    path('guest_register/', guest_register.as_view(), name='guest_register'),
    path('resident_register/', resident_register.as_view(), name='resident_register'),
    path('login/', login_request, name='login'),
   
    path('account/', account_view, name="account"),

    path('report/', report_detail_view, name="report"),
    #bill
    path('bill/', bill_detail_view, name="bill"),
  
    path('buying/', buy_view, name="buying"),
    #emergency
    path('allemergency/', allemergency_detail_view, name="allemergency"),
    #all bill
    path('allbill/', allbill_detail_view, name="allbill"),
    path('recpt/', rept_view, name="recpt"),
    path('checkfacility/', checkfacility_view, name="checkfacility"),

    path('guestcheckfacility/', guestcheckfacility, name="guestcheckfacility"),
    path('roombooking/', checkavil, name="checkavil"),
    #url fro notification
    path('notifications/', notifications, name='notifications'),


    path('contact/', contact_detail_view, name="contact"),
    path('emergency/', emergency_detail_view, name="emergency"),
    path('emergencyguest/', emergency_detail, name="emergencyguest"),
    path('guest/', guest_screen_view, name="guest"),
    path('guest1/', guest_screen, name="guest1"),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='myapp/registration/password_change_done.html'), 
        name='password_change_done'),
  
    
    #canclebboking
    path('profile/', newprofile, name='profile'),

    #profile
    path('profile1/', profile, name='profile1'),
  


    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='myapp/registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='myapp/registration/password_reset_complete.html'),
     name='password_reset_complete'),
     
  
    path('about', views.aboutpage,name="aboutpage"),
    path('contact/', views.contactpage,name="contactpage"),
    path('user', views.user_log_sign_page,name="userloginpage"),
    path('user/login', views.user_log_sign_page,name="userloginpage"),
    path('user/bookings', views.user_bookings,name="dashboard"),
    path('user/roombooking/', checkavil, name="checkavil"),
    path('user/book-room', views.book_room_page,name="bookroompage"),
    path('user/book-room/book', views.book_room,name="bookroom"),
    path('user/signup', views.user_sign_up,name="usersignup"),
    path('staff/', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/login', views.staff_log_sign_page,name="staffloginpage"),
    path('staff/signup', views.staff_sign_up,name="staffsignup"),
    path('logout1', views.logoutuser,name="logout1"),
    path('staff/panel', views.panel,name="staffpanel"),
    path('staff/allbookings', views.all_bookings,name="allbookigs"),
    
    path('staff/panel/add-new-location', views.add_new_location,name="addnewlocation"),
    path('staff/panel/edit-room', views.edit_room),
    path('staff/panel/add-new-room', views.add_new_room,name="addroom"),
    path('staff/panel/edit-room/edit', views.edit_room),
    path('staff/panel/view-room', views.view_room),
    #delete
    #path('user/booking/<int:pk>/delete_order', CancelBookingView.as_view(), name="delete_order"),
    #contaxct
     # path('book_list/', BookingListView.as_view(), name='BookingList'),
    #  path('room_list/', RoomList.as_view(), name='RoomList'),
    #path('allreport', allreport, name="allreport"),
   # path('booking/cancel/<pk>', CancelBookingView.as_view(), name='CancelBookingView')
       # path('login/', login_view, name="login"),
     # path('buy/', buy_screen_view, name="buy"),
      #  path('book/', BookingView.as_view(), name='book'),
       #hotel booking
    #path('delete_order/<str:pk>/', views.deletebooking, name="delete_order"),
    #path('', index_screen_view, name="home"),
   # path('room/', RoomListView.as_view(), name="room"),
  #  path('add_booking/', booking_detail_view, name="booking"),
   # path('changeroom/', change_room_view, name="changeroom"),
    # path('buy/', buy_screen_view, name="buy"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)