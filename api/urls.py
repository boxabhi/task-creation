
from rest_framework import routers
from home.views import TaskViewSet
from django.urls import path

router = routers.SimpleRouter()

router.register(r'task', TaskViewSet)




urlpatterns = [
  
]

urlpatterns += router.urls