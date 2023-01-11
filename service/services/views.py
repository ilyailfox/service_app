from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from services.models import Subscription


class SubscriptionView(ReadOnlyModelViewSet):
    queryset = Subscription.object.all()
