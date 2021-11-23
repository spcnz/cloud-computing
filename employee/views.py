from .models import Employee
from django.http import JsonResponse, HttpResponse


def get_all(request):
    data = Employee.objects.all()
    
    return JsonResponse(data, safe=False, status=200)
