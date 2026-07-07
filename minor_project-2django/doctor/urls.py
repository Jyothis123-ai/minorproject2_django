from django.urls import path
from . import views

urlpatterns = [
    # Template Views
    path('', views.doctor, name='doctor'),
    path('details/', views.doctor_details, name='doctor_details'),
    path('profile/', views.doctor_profile, name='doctor_profile'),
    path('contact/', views.doctor_contact, name='doctor_contact'),

    # APIs
    path('api/', views.doctor_api, name='doctor_api'),
    path('api/details/', views.doctor_api_details, name='doctor_api_details'),
    path('api/add/', views.doctor_api_add, name='doctor_api_add'),
    path('api/update/', views.doctor_api_update, name='doctor_api_update'),
    path('api/delete/', views.doctor_api_delete, name='doctor_api_delete'),

    # Dynamic URLs (must come last to avoid catching other paths)
    path('<int:id>/', views.doctor_by_id, name='doctor_by_id'),
    path('<str:name>/', views.doctor_by_name, name='doctor_by_name'),
]
