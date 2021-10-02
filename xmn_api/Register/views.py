import uuid
from rest_framework import serializers, status
from django.shortcuts import render
from h11 import Response

from . import serializers
from .models import User
from .serializers import UserSerializers
from rest_framework import generics
from rest_framework.response import Response
# Create your views here.
class UserApiView(generics.GenericAPIView):
    serializer_class = UserSerializers

    def post(self,request):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if serializer.is_valid():
            serializer.save()
            return Response({
                 "RequestId":str(uuid.uuid4()),
                "Message":"Usercreated successfully",

                'User':serializer.data}
            )
        return Response({"Errors":serializer.errors},status=status.HTTP_400_BAD_REQUEST)