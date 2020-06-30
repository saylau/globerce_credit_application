from django.http import Http404
from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from globerce_credit_application.credit_application.models import CreditApplication
from globerce_credit_application.credit_application.serializers import CreditApplicationSerializer, CreateCreditApplicationSerializer
from globerce_credit_application.users.permissions import IsUserOrReadOnly


class CreditApplicationViewSet(APIView):
    """
    Check credit applications status
    """
    
    permission_classes = (AllowAny,)

    def get(self, request, id, format=None):
        try:
            credit_application = CreditApplication.objects.get(id=id)
            serializer = CreditApplicationSerializer(credit_application)
            return Response(serializer.data)
        except:
            raise Http404



class CreateCreditApplicationViewSet(mixins.CreateModelMixin,
                        viewsets.GenericViewSet):
    """
    Creates credit appliciation
    """
    queryset = CreditApplication.objects.all()
    serializer_class = CreateCreditApplicationSerializer
    permission_classes = (AllowAny,)
