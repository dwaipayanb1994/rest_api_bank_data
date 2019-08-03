from django.contrib import admin
from django.urls import path
# from .views import BranchByIFSC, BranchByBankAndCity
from .views import AccessDB

urlpatterns = [
    # path('ifsc/<str:ifsc>/', BranchByIFSC, name="ifsc"),
    # path('bank_city/<str:bank>/<str:city>/', BranchByBankAndCity, name="branchbycity")
    path('', AccessDB, name="access_db"),
]
