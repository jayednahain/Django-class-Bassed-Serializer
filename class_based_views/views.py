
from django.shortcuts import render

from class_based_views.models import Student
from class_based_views.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView #useing for class based views !

from django.http import Http404

class StudentListView(APIView):

   #this class will do only non primary key based operations!
   # StudentListView extend or inherite the APIview !

   def get(self,request): #vew all the student data
      students = Student.objects.all()
      serializer = StudentSerializer(students,many=True)
            #serilizing the data from database and return it
      return Response(serializer.data)


   def post(self,request): #craete a student !
      serializer = StudentSerializer(data=request.data)
               #getting data from web and serilize it !
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class for primary key based operations
class StudentDetailView(APIView):
   def get_object(self,pk):
      try:
         return Student.objects.get(pk = pk)
      except Student.DoesNotExist:
         raise Http404
         #insted of "return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)"


   def get(self,request,pk):
      student = self.get_object(pk)
               #using get_object method and pass the primary key
               #to get the specific student !

      serializer=StudentSerializer(student)
      return Response(serializer.data)

   def put(self,request,pk): #update data
      student = self.get_object(pk)
      serializer = StudentSerializer(student,data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


   def delet(self,request,pk):
      student = self.get_object(pk)
      student.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)

