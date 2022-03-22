from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from Individual.models import User
from ShelterProvider.models import postData
from .serializers import ShelterUserSerializer
# Create your views here.
class ShelterUserViewSet(viewsets.ViewSet):
    def list(self,request):
        user = User.objects.filter(is_shelter=True)
        serializer = ShelterUserSerializer(user,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk):
        if pk is not None:
            try:
                user = User.objects.exclude(is_superuser=True,is_individual=True,is_organization=True).get(id=pk)
                serializer = ShelterUserSerializer(user)
                return Response(serializer.data)
            except:
                return Response({"Error":"Data not found!"},status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({"Error":"Define none as id!"},status=status.HTTP_400_BAD_REQUEST)
    def create(self,request):
        serializer = ShelterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(sef,request,pk):
        user = User.objects.get(id=pk)
        serializer = ShelterUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Partial Updated"},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({"msg":"Fail"},status=status.HTTP_204_NO_CONTENT)
    def destroy(self,request,pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response({"msg":"Sucessfully delete"})
    

class ShelterEditUserViewSet(viewsets.ViewSet):

    def retrieve(self, request,pk):
        if pk is not None:
            try:
                user = postData.objects.get(id=pk)
                serializer = ShelterUserSerializer(user)
                return Response(serializer.data)
            except:
                return Response({"Error":"Data not found!"},status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({"Error":"Define none as id!"},status=status.HTTP_400_BAD_REQUEST)
    
    def create(self,request):
        serializer = ShelterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(sef,request,pk):
        user = User.objects.get(id=pk)
        serializer = ShelterUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Partial Updated"},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({"msg":"Fail"},status=status.HTTP_204_NO_CONTENT)