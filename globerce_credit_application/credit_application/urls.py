from django.urls import path

from globerce_credit_application.credit_application.views import CreditApplicationViewSet, CreateCreditApplicationViewSet

app_name = 'cars'

urlpatterns = [
    path('<int:id>/', CreditApplicationViewSet.as_view()),
    path('create/', CreateCreditApplicationViewSet.as_view({'post': 'create'})),
]
