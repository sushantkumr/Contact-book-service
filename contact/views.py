from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import status
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactSerializer
from rest_framework.permissions import IsAuthenticated


class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all().order_by('id')
    serializer_class = ContactSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'email')
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)
