from django.urls import path
from .views import contact_view,render

urlpatterns = [
    path('', contact_view, name='contact'),
    path('success/', lambda request: render(request, 'contact/success.html'), name='contact_success'),
]
