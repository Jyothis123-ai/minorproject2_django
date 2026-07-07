from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# ---- Template Views ----

def doctor(request):
    return render(request, "doctor.html")

def doctor_details(request):
    return render(request, "doctor_details.html")

def doctor_profile(request):
    return render(request, "doctor_profile.html")

def doctor_contact(request):
    return render(request, "doctor_contact.html")

# ---- Dynamic URL Views ----

def doctor_by_id(request, id):
    return HttpResponse(f"Doctor ID : {id}")

def doctor_by_name(request, name):
    return HttpResponse(f"Doctor Name : {name}")

# ---- API Views ----

def doctor_api(request):
    return JsonResponse({"message": "Welcome to Doctor API"})

def doctor_api_details(request):
    data = {
        "doctor_id": "D101",
        "doctor_name": "Dr. Ramesh Kumar",
        "specialization": "Cardiologist",
        "experience": "12 Years",
        "hospital": "City Hospital",
    }
    return JsonResponse(data)

@csrf_exempt
def doctor_api_add(request):
    if request.method == "POST":
        return JsonResponse({"message": "Doctor Added Successfully"})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)

@csrf_exempt
def doctor_api_update(request):
    if request.method == "PUT":
        return JsonResponse({"message": "Doctor Updated Successfully"})
    return JsonResponse({"error": "Only PUT method allowed"}, status=405)

@csrf_exempt
def doctor_api_delete(request):
    if request.method == "DELETE":
        return JsonResponse({"message": "Doctor Deleted Successfully"})
    return JsonResponse({"error": "Only DELETE method allowed"}, status=405)
