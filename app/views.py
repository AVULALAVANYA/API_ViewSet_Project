from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ViewSet
from app.models import *
from app.serializers import *
from rest_framework.response  import Response
class ProductCrudVS(ViewSet):
    def list(self,request):
        PQS=Product.objects.all()
        PSD=ProductSerializer(PQS,many=True)
        return Response(PSD.data)
    def create(self,request):
        SD=ProductSerializer(data=request.data)
        if SD.is_valid():
            SD.save()
            return Response({'success':'product is created'})
        else:
            return Response({'failed':'not valid product'})

    def retrieve(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO)
        return Response(SPD.data)

    def update(self,request,pk):
        SPO=Product.objects.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data)
        if SPD.is_valid():
            SPD.save()
            return Response({'update':'product is updated'})
        else:
            return Response({'failed':'product is not valid'})
    def partial_update(self,request,pk):
        SPO=Product.object.get(pk=pk)
        SPD=ProductSerializer(SPO,data=request.data,partial=True)
        if SPD.is_valid():
            SPD.save()
            return Response({'update':'product is updated'})
        else:
            return Response({'failed':'product is not valid'})

    def destroy(self,request,pk):
        Product.object.get(pk=pk).delete()
        return Response({'Deleted':'product is deleted'})