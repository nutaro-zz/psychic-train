from rest_framework.serializers import IntegerField,\
                                       ModelSerializer,\
                                       StringRelatedField

from api.models import Client, Email, Phone


class PhoneSerializer(ModelSerializer):

    country_code = StringRelatedField(label='country', many=False)
    area_code = StringRelatedField(label='area', many=False)
    number = StringRelatedField(many=False)
    type = StringRelatedField(many=False)


    class Meta:
        model = Phone
        fields = ['id', 'country', 'area', 'number', 'type']


class EmailSerializer(ModelSerializer):

    email = StringRelatedField(many=False)

    class Meta:
        model = Email
        fields = ['id', 'email']



class ClientSerializer(ModelSerializer):

    name = StringRelatedField(many=False)
    email = EmailSerializer(many=True, read_only=True)
    phone = PhoneSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'email', 'phone']
