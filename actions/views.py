from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ActionSerializer
from .models import Action
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
