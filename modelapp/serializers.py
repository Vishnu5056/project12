from rest_framework import serializers
class ProductSerializer(serializers.Serializer):
    pid=serializers.IntegerField()
    pname=serializers.CharField(max_length=20)
    pcost=serializers.DecimalField(max_digits=10,decimal_places=2)
    pmfdt=serializers.DateField()
    pexpdt=serializers.DateField()
