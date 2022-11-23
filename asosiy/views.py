from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

class SuvlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        suv=Suv.objects.all()
        serializer = SuvSerializer(suv, many=True)

        return Response(serializer.data)
    def post(self,request):
        suv = request.data
        serializer = SuvSerializer(data=suv)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "qoshilgan malumot":serializer.data}
            return Response(natija, status=status.HTTP_201_CREATED)
        return Response({"xabar":"Ma'lumotda xatolik bor!"})

class SuvAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        suv = Suv.objects.get(id=pk)
        serializer = SuvSerializer(suv,data=request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "yangi malumot":serializer.data}
            return Response(natija)
        return Response({"xabar":"Ma'lumotda xatolik bor!"})
    def delete(self,request,pk):
        suv=Suv.objects.get(id=pk)
        suv.delete()
        return Response({"xabar":"Ma'lumot ochirib yuborildi!"})

class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        mijozlar=Mijoz.objects.all()
        serializer = MijozSerializer(mijozlar, many=True)

        return Response(serializer.data)
    def post(self,request):
        mijozlar = request.data
        serializer = MijozSerializer(data=mijozlar)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "qoshilgan malumot":serializer.data}
            return Response(natija, status=status.HTTP_201_CREATED)
        return Response({"xabar":"Ma'lumotda xatolik bor!"})

class MijozAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self,request,pk):
        mijoz = Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz,data=request.data)
        if serializer.is_valid():
            serializer.save()
            natija = {"xabar":"Saqlandi!",
                      "yangi malumot":serializer.data}
            return Response(natija)
        return Response({"xabar":"Ma'lumotda xatolik bor!"})
    def delete(self,request,pk):
        mijoz=Mijoz.objects.get(id=pk)
        mijoz.delete()
        return Response({"xabar":"Ma'lumot ochirib yuborildi!"})

class AdminlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        adminlar = Admin.objects.all()
        serializer = AdminSerializer(adminlar, many=True)
        return Response(serializer.data)
class AdminAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        admin = Mijoz.objects.get(id=pk)
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data)

class HaydovchilarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        haydovchilar = Haydovchi.objects.all()
        serializer = HaydovchiSerializer(haydovchilar, many=True)
        return Response(serializer.data)
class HaydovchiAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        haydovchi = Haydovchi.objects.get(id=pk)
        serializer = HaydovchiSerializer(haydovchi, many=True)
        return Response(serializer.data)
class BuyurtmalarAPIView(APIView):
    def get(self, request):
        suvlar=Buyurtma.objects.filter(admin__user=request.user)|Buyurtma.objects.filter(mijoz__user=request.user)
        serializer=BuyurtmaSerializer(suvlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        suv=request.data
        serializer=BuyurtmaSerializer(data=suv)
        if serializer.is_valid():
            serializer.save(mijoz=Mijoz.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)






