from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Q


def index(request):
    return render(request, 'index.html')


def login_page(request):
    return render(request, 'login.html')

def registration(request):
    if request.method == "POST":
        username =request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('email')

        # if User.objects.filter(
        #     Q(username = username) | 
        #     Q(email = email)
        #     ).exists():
        #     return redi
        

    return render(request, 'resgitration.html')

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def list(self, request):
        serializer = TaskSerializer(self.queryset.order_by('index'), many = True)
        return Response(serializer.data)
        return super().list(request, *args, **kwargs)
    
    def delete(self , request):
        data = request.data
        print(data)
        if data.get('uid'):
            task = Task.objects.filter(uid =data.get('uid') ).delete()
            return Response({
                "message" : "Task deleted"
            })
        return Response({
                "message" : "uid is required"
            })
        
        


