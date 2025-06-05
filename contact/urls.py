from django.urls import path
from .views import contact_view,render,register_view,login_view,logout_view,home_view

urlpatterns = [
    path('', home_view, name='home'),  # root URL shows home page now
    path('contact/',contact_view, name='contact_form'),  # contact form at /contact/
    path('success/', lambda request: render(request, 'contact/success.html'), name='contact_success'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]
