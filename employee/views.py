from .models import Employee, Counter
from django.http import JsonResponse
from .serializer import EmployeeSerializer, CounterSerializer


def get_all(request):
    data = Employee.objects.all()
    serializer = EmployeeSerializer(data, many=True)
    
    return JsonResponse(serializer.data, safe=False, status=200)

def inc_counter(request):
    counter = Counter.objects.filter().first()
    if (not counter):
        counter = Counter.objects.create()
    counter.value += 1
    counter.save()

    serializer = CounterSerializer(counter)
    return JsonResponse(serializer.data, status=200)