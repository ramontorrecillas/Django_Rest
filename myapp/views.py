from django.shortcuts import render

# Create your views here.
from .models import Officeitems,Postalcodes
from .serializers import OfficeItemsSerializer
from .serializers import PostalCodeSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class OfficeList(APIView):
	"""
	List all office madrid
	"""
	def getPostalCode(self,cp):
		try:
			return Postalcodes.objects.filter(idpostalcode=cp)
		except Postalcodes.DoesNotExist:
			raise Http404
			

	def get(self,request,cp,format=None):
		items = self.getPostalCode(cp)
		serializer = PostalCodeSerializer(items, many=True)
		return Response(serializer.data)

