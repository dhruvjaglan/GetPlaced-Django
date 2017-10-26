from rest_framework import serializers
from .models import *

class ApplicantSerializer(serializers.ModelSerializer):
	class Meta:
		model = applicant_detail
		fields = '__all__'


class OffersSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = company_offer
		fields = '__all__'

class CompanyLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = company
		fields = ('userid', 'password')


class CompanySerializer(serializers.ModelSerializer):
	offers = OffersSerializer(read_only=True, many=True)

	class Meta:
		model = company
		fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
	offers = OffersSerializer(read_only=True, many=True)

	class Meta:
		model = student
		fields = '__all__'


class QuerySerializer(serializers.ModelSerializer):
	class Meta:
		model=query
		fields='__all__'		
