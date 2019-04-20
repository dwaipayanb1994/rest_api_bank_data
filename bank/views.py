from django.shortcuts import render
from .models import Bank, Branch
from .serializers import BankSerializer
from rest_framework.response import Response
from django.http import JsonResponse

# Create your views here.

def BranchByIFSC(request, ifsc):
    try:
        data = Branch.objects.get(ifsc=ifsc)
    except Branch.DoesNotExist:
        data = None
    serialized_data = BankSerializer(data)
    return JsonResponse(serialized_data.data, safe=False)

def BranchByBankAndCity(request, bank, city):
    data = Branch.objects.filter(city=city, bank_id__name__exact=bank)
    serialized_data = BankSerializer(data, many=True)
    return JsonResponse(serialized_data.data, safe=False)
