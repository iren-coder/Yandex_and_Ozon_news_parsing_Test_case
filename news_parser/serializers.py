from news_parser.models import News 
from rest_framework import serializers  


class NewsSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = News  
        fields = '__all__'