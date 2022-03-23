from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from ShelterProvider.models import postData,preData
from .serializers import ShelterUserSerializer,ShelterUserResponseSerializer
# Create your views here.


class search(viewsets.ViewSet):
    def retrieve(self, request,pk):
        if pk is not None:
            try:
                user = list(preData.objects.filter(city=pk).values("shelter_name","address","city","total_beds"))
                return Response(user)
            except:
                return Response({"Error":"Data not found!"},status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({"Error":"Define none as id!"},status=status.HTTP_400_BAD_REQUEST)
    
            
class ShelterUserViewSet(viewsets.ViewSet):
    def list(self,request):
        user = preData.objects.all()
        serializer = ShelterUserSerializer(user,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk):
        if pk is not None:
            try:
                user = preData.objects.get(id=pk)
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
        user = preData.objects.get(id=pk)
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
        user = postData.objects.get(id=pk)
        serializer = ShelterUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Partial Updated"},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({"msg":"Fail"},status=status.HTTP_204_NO_CONTENT)