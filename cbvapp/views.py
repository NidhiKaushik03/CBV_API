from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from .models import Course, CourseSerializer
from rest_framework import mixins, generics
from rest_framework.viewsets import ViewSet, ModelViewSet

# class CourseListView(APIView):
#     def get(self, request):
#         course = Course.objects.all()
#         serializer = CourseSerializer(course , many=True)
#         return Response(serializer.data)
    
#     def post(self, request):
#         courseserializer = CourseSerializer(data = request.data)
#         if courseserializer.is_valid():
#             courseserializer.save()
#             return Response(courseserializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(courseserializer.errors)

class CourseDetailsView(APIView):
    def get_course(self,  pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
       
    

    def get(self, request, pk):
        course = self.get_course(pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)            
    def delete(self, request, pk):
        self.get_course(pk).delete()
        return Response(status= status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        course = self.get_course(pk)
        courseserializer = CourseSerializer(data = request.data)
        if courseserializer.is_valid():
            courseserializer.save()
            return Response(courseserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(courseserializer.errors)
          