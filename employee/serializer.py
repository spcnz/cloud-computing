from django.db.models import fields
from rest_framework import serializers
from .models import Employee, Counter


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'name', 'surname', 'salary', 'birth_date']

class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ['value']