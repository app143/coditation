from rest_framework import serializers
from empyloeeapi.models import product,category,child_product


# class productSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=product
#         fields = '__all__'


class productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=product
        fields = ('id','url','name','brand','location')
        

class categorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=category
        fields = ('id','url','name',' category_name',' category_no')
        

class child_productSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=child_product
        fields = ('id','url','child_product_name','child_product_no')