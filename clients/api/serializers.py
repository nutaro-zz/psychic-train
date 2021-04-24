from rest_framework import serializers

from api.models import Client

class ClientSerializer(serializers.ModelSerializer):

    phones = serializers.StringRelatedField(many=True)
    email = serializers.StringRelatedField(many=False)

    class Meta:
        model = Client
        fields = ['name', 'gender', 'id_card',
                  'social_security_number', 'birth_date',
                  'phones', 'email']
