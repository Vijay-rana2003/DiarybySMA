from django.urls import path
from home import views
urlpatterns=[
    path('',views.index,name="index"),
    path('contact/',views.contactus,name="contactus"),
    path('diarypage/',views.diarypage,name="mydiary"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('login/',views.handlelogin,name="login"),
    path('logout/',views.handlelogout,name="logout"),
    path('signup/',views.handlesignup,name='signup'),
    path('search/',views.search,name="search"),
    path('read/<int:sno>',views.viewdiarypage,name='readdiary'),
    path('update/<int:sno>',views.updatediary,name='updatediary'),
    path('delete/<int:sno>',views.deletediarypage,name='deletediary'),
]