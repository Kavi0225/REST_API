from rest_framework import serializers
from students.models import Student, Employee
from Blogs.models import Blogss, Comments

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

class EmplyoeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"



class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"

class BlogsSerializer(serializers.ModelSerializer):
    comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = Blogss
        fields = "__all__"
        