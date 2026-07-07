from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

# ---- Template Views ----

def patient(request):
    return render(request, "patient.html")

def patient_details(request):
    return render(request, "patient_details.html")

def patient_report(request):
    return render(request, "patient_report.html")

def patient_bill(request):
    return render(request, "patient_bill.html")

# ---- Dynamic URL Views ----

def patient_by_id(request, id):
    return HttpResponse(f"Patient ID : {id}")

def patient_by_name(request, name):
    return HttpResponse(f"Patient Name : {name}")

# ---- API Views ----

def patient_api(request):
    return JsonResponse({"message": "Welcome to Patient API"})

def patient_api_details(request):
    data = {
        "patient_id": "P201",
        "patient_name": "Rahul Sharma",
        "age": 28,
        "gender": "Male",
        "disease": "Viral Fever",
    }
    return JsonResponse(data)

@csrf_exempt
def patient_api_add(request):
    if request.method == "POST":
        return JsonResponse({"message": "Patient Added Successfully"})
    return JsonResponse({"error": "Only POST method allowed"}, status=405)

@csrf_exempt
def patient_api_update(request):
    if request.method == "PUT":
        return JsonResponse({"message": "Patient Updated Successfully"})
    return JsonResponse({"error": "Only PUT method allowed"}, status=405)

@csrf_exempt
def patient_api_delete(request):
    if request.method == "DELETE":
        return JsonResponse({"message": "Patient Deleted Successfully"})
    return JsonResponse({"error": "Only DELETE method allowed"}, status=405)
