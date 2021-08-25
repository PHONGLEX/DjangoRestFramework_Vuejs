from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.http import JsonResponse

from .models import Psi, AirTemperature
from .serializers import PsiSerializer, AirTemperatureSerializer


class PsiViewSet(ModelViewSet):
	serializer_class = PsiSerializer
	permission_classes = (IsAuthenticated,)
	queryset = Psi.objects.all()

	def list(self, queryset):
		data = Psi.objects.all().values()
		return JsonResponse(list(data), safe=False)


class AirTemperatureViewSet(ModelViewSet):
	serializer_class = AirTemperatureSerializer
	permission_classes = (IsAuthenticated,)
	queryset = Psi.objects.all()

	def list(self, queryset):
		data = AirTemperature.objects.all().values()
		return JsonResponse(list(data), safe=False)
