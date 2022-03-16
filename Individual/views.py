from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from Individual.models import User
from Individual.serializers import IndividualUserSerializer
# Create your views here.
class IndividualUserViewSet(viewsets.ViewSet):
    def list(self,request):
        user = User.objects.exclude(is_superuser=True).all()
        serializer = IndividualUserSerializer(user,many=True)
        return Response(serializer.data)
    
    def retrieve(self, request,pk):
        if pk is not None:
            try: 
                user = User.objects.exclude(is_superuser=True).get(id=pk)
                serializer = IndividualUserSerializer(user)
                return Response(serializer.data)
            except:
                return Response({"Error":"Data not found!"},status=status.HTTP_400_BAD_REQUEST)
                
        else:
            return Response({"Error":"Define none as id!"},status=status.HTTP_400_BAD_REQUEST)
    def create(self,request):
        serializer = IndividualUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def partial_update(sef,request,pk):
        user = User.objects.get(id=pk)
        serializer = IndividualUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Data Partial Updated"},status=status.HTTP_206_PARTIAL_CONTENT)
        return Response({"msg":"Fail"},status=status.HTTP_204_NO_CONTENT)
    def destroy(self,request,pk):
        user = User.objects.get(id=pk)
        user.delete()
        return Response({"msg":"Sucessfully delete"})
