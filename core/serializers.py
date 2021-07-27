# core/serializers.py
from rest_framework import serializers

from .models import *


class BranchSerializer(serializers.ModelSerializer):

	creator = serializers.ReadOnlyField(source='created_by.email')

	class Meta:
		model = Branch
		fields = ('id','name', 'creator')
   

class DepartmentSerializer(serializers.ModelSerializer):

	creator = serializers.ReadOnlyField(source='created_by.username')

	class Meta:
		model = Department
		fields = ('id','name', 'branch', 'creator','created',)
   

class ProductSerializer(serializers.ModelSerializer):

	creator = serializers.ReadOnlyField(source='created_by.username')
	class Meta:
		model = Product
		fields = ('id','name', 'price','department','creator',)
