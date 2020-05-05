from apps.dreamjarmaker.models import Dream
from apps.dreamjarmaker.serializers import DreamSerializer
from rest_framework import generics

class DreamJarListCreateView(generics.ListCreateAPIView):
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer
    def perform_create(self, serializer):
        serializer.save() 

class DreamJarDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dream.objects.all()
    serializer_class = DreamSerializer