

from django.contrib import admin
from django.urls import path,reverse_lazy
from myapp import views
from django.contrib.auth.views import (LogoutView,
                                       LoginView,

                                       PasswordChangeView,
                                       PasswordChangeDoneView,

                                       PasswordResetView,
                                       PasswordResetDoneView,
                                       PasswordResetConfirmView,
                                       PasswordResetCompleteView)



app_name ='myapp'


urlpatterns = [
    path('',views.home,name='home'),
    path('<int:val>/',views.detail,name='detail'),


    path('add/',views.add_new,name='add_new'),
    path('<int:val>/edit/',views.edit_form,name='edit_form'),


    path('login/',LoginView.as_view(),name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/',LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    path('password-change/',PasswordChangeView.as_view(success_url=reverse_lazy('myapp:password-change-done')),name='password-change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='registration/password-change-done.html'), name='password-change-done'),

    path('password-rest/',PasswordResetView.as_view(success_url=reverse_lazy('myapp:password-rest-done')),name='password-rest'),
    path('password-rest/done/', PasswordResetDoneView.as_view(),name='password-rest-done'),
    path('rest/<uidb64>/<token/>',PasswordResetConfirmView.as_view(),name='password-rest-confirm'),
    path('password-rest/complete/', PasswordResetCompleteView.as_view(), name='password-rest-complete'),

]

