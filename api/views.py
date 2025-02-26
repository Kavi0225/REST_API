from django.shortcuts import render, get_object_or_404
# from django.http import JsonResponse
from .models import *
from students.models import Student, Employee
from Blogs.models import Blogss, Comments
from .serializers import StudentSerializer, EmplyoeeSerializer, BlogsSerializer, CommentsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from .paginations import *
from .filter import EmployeeFilters
from django_filters.rest_framework import DjangoFilterBackend

# from dja
# from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
# Create your views here.

@api_view(['GET','POST'])
def studentsView(request):
    if request.method =='GET':
        # get all the data form table
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT', 'DELETE'])
def studentDetailsViews(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer  = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = StudentSerializer(student,data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

# class EmployeesView(APIView):
#     def get(self, request):
#         # get all the data form table
#         employee = Employee.objects.all()
#         serializer = EmplyoeeSerializer(employee, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
#     def post(self, request):
#         serializer = EmplyoeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         print(serializer.errors)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EmployeedetailsViews(APIView):
#     def get_object(self, pk):
#         try:
#             return Employee.objects.get(pk=pk)
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):

#         employee = self.get_object(pk)
#         serializer  = EmplyoeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmplyoeeSerializer(employee,data=request.data) 
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class EmployeesView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmplyoeeSerializer
    
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)


# class EmployeedetailsViews(RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin,GenericAPIView):
    
#     queryset = Employee.objects.all()
#     serializer_class = EmplyoeeSerializer

#     def get(self, request, pk):
#         return self.retrieve(request, pk)

#     def put(self,request, pk):
#         return self.update(request, pk)

#     def delete(self, request, pk):
#         return self.destroy(request, pk)
    

# class EmployeesView(generics.ListCreateAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmplyoeeSerializer

# class EmployeedetailsViews(generics.RetrieveUpdateDestroyAPIView):
    
#     queryset = Employee.objects.all()
#     serializer_class = EmplyoeeSerializer
#     lookup_field = 'pk'

# class EmployeesViewset(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Employee.objects.all()
#         serializer = EmplyoeeSerializer(queryset, many=True)
#         return Response(serializer.data)
    
#     def create(self, request):
#         serializer = EmplyoeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
    
#     def retrieve(self, request,pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmplyoeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def update(self, request, pk=None):
#         employee = get_object_or_404(Employee, pk=pk)
#         serializer = EmplyoeeSerializer(employee)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def destroy(self, request, pk=None):
#         employee = get_object_or_404(Employee,pk=pk)
#         employee.delete()
#         serializer = EmplyoeeSerializer(employee) 
#         return Response(serializer.data,status=status.HTTP_204_NO_CONTENT)


class EmployeesViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmplyoeeSerializer
    filter_backends =[DjangoFilterBackend]
    filterset_class = EmployeeFilters


class BlogsViewsSet(viewsets.ModelViewSet):
    queryset = Blogss.objects.all()
    serializer_class = BlogsSerializer

class CommentViewsSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    pagination_class = CustomPaginations
    
class BlogDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogss.objects.all()
    serializer_class = BlogsSerializer
    lookup_field = 'pk'

class CommentDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = 'pk'
