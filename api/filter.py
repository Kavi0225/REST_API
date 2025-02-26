import django_filters
from students.models import Employee

class EmployeeFilters(django_filters.FilterSet):
    emp_name = django_filters.CharFilter(field_name='emp_name',lookup_expr='icontains')
    emp_branch = django_filters.CharFilter(field_name='emp_branch',lookup_expr='icontains')
    class Meta:
        model = Employee
        fields = ['emp_name', 'emp_branch']
        