from .models import Branch
from rest_framework import serializers

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = "__all__"
