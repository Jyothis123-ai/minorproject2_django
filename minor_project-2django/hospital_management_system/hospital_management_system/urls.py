from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <h2>Hospital Management System</h2>
        <ul>
            <li><a href='/doctor/'>Doctor Module</a></li>
            <li><a href='/patient/'>Patient Module</a></li>
        </ul>
    """)

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('doctor/', include('doctor.urls')),
    path('patient/', include('patient.urls')),
]
