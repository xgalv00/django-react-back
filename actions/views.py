from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ActionSerializer
from .models import Action


class ActionViewSet(viewsets.ModelViewSet):
    queryset = Action.objects.all()
    serializer_class = ActionSerializer
