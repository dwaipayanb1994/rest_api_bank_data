from django.shortcuts import render
import pymysql.cursors
# from .models import Bank, Branch
# from .serializers import BankSerializer
from rest_framework.response import Response
from django.http import JsonResponse
from django.http import HttpResponseNotFound


# Create your views here.

def AccessDB(request):
    x = request.GET.get('x', '')
    y = request.GET.get('y', '')
    query_rest = request.GET.get('q', '')

    """ Generate query """
    query = "SELECT " + x + " FROM all_data"

    """ Add filter """
    if not query_rest:
        query += query_rest

    """ Create each column """
    query += " GROUP BY " + x

    connection = pymysql.connect(host='milkdatabase.csk3krdyw7j7.eu-west-1.rds.amazonaws.com',
                             user='admin',
                             password='password',
                             db='milkbasket',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    print(query)
    try:
        with connection.cursor() as cursor:
            # Read a single record
            # sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
            cursor.execute(query)
            result = cursor.fetchall()
            print(type(result[0]))
            return JsonResponse(result, safe=False)
    finally:
        connection.close()
    return HttpResponseNotFound("hello")


# def BranchByBankAndCity(request, bank, city):
#     data = Branch.objects.filter(city=city, bank_id__name__exact=bank)
#     serialized_data = BankSerializer(data, many=True)
#     return JsonResponse(serialized_data.data, safe=False)
