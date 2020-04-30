from rest_framework import serializers
from rest_framework_jwt.serializers import User

from api.models import Company, Vacancy


class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    city = serializers.CharField()
    address = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data['name'], description=validated_data['description'],
                                         city=validated_data['city'], address=validated_data['address'])
        company.save()
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.city = validated_data['city']
        instance.address = validated_data['address']
        instance.save()
        return instance


class VacancySerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company')



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
