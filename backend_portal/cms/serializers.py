from rest_framework import serializers

#from .models import Category, Section, Content, Post, Comment
from .models import About, Homepage, AreaBigCategory, SpecificArea, Opportunity

class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'

class HomepageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Homepage
        fields = '__all__'

class AreaBigCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = AreaBigCategory
        fields = '__all__'

class SpecificAreaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SpecificArea
        fields = '__all__'

class OpportunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Opportunity
        fields = '__all__'
