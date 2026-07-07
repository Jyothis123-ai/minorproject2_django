from django.urls import path
from . import views

urlpatterns = [
    # Template Views
    path('', views.patient, name='patient'),
    path('details/', views.patient_details, name='patient_details'),
    path('report/', views.patient_report, name='patient_report'),
    path('bill/', views.patient_bill, name='patient_bill'),

    # APIs
    path('api/', views.patient_api, name='patient_api'),
    path('api/details/', views.patient_api_details, name='patient_api_details'),
    path('api/add/', views.patient_api_add, name='patient_api_add'),
    path('api/update/', views.patient_api_update, name='patient_api_update'),
    path('api/delete/', views.patient_api_delete, name='patient_api_delete'),

    # Dynamic URLs (must come last to avoid catching other paths)
    path('<int:id>/', views.patient_by_id, name='patient_by_id'),
    path('<str:name>/', views.patient_by_name, name='patient_by_name'),
]
