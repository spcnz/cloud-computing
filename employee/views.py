from .models import Employee
from django.http import JsonResponse
from .serializer import EmployeeSerializer


def get_all(request):
    data = Employee.objects.all()
    serializer = EmployeeSerializer(data, many=True)
    
    return JsonResponse(serializer.data, safe=False, status=200)
