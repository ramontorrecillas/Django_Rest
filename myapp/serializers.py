from rest_framework import serializers
from myapp.models import Officeitems
from myapp.models import Postalcodes

class OfficeItemsSerializer(serializers.ModelSerializer):


	class Meta:
		model = Officeitems
		fields = ['idoffice','addresslocality','addressregion','streetaddress','description',
		'description','name','telephone','openinghours','latitude','longitude','url']
		ordering=['idoffice']

class PostalCodeSerializer(serializers.ModelSerializer):

	items = OfficeItemsSerializer(many=True,read_only=True)

	class Meta:
		model = Postalcodes
		fields = ['idpostalcode','holidays','items']
