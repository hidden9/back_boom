# Django Import
from django.shortcuts import render
from django.http import JsonResponse
# from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status
from Boom.models import Artist , Expert , Expert_comment , Artwork_advertisement , Customer , Sample_artwork  , Order_counter
from django.shortcuts import render,redirect
from Boom.serializers import advertisementCreate
# Rest Framework Import
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.response import Response
# from rest_framework.serializers import Serializer
from rest_framework import generics , permissions
# from rest_framework.authtoken.models import Token
# from rest_framework.viewsets import ModelViewSet
from knox.models import AuthToken
# from rest_framework.permissions import AllowAny
# from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
# Rest Framework JWT
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework_simplejwt.views import TokenObtainPairView
#Local import

# from ..models import Artist , Expert , Artwork_advertisement , Customer
from ..serializers import RegisterCustomerSerializer, RegisterExpertSerializer , RegisterArtistSerializer  , UserSerializer  ,LoginSerializers, ArtistSerializer , ExpertSerializer , CustomerSerializer , LogInSerializer
from rest_framework import permissions
from Boom.permissions import *
from django.contrib.auth import get_user_model

User = get_user_model()




# class RegisterArtistAPI(generics.GenericAPIView):
#     serializer_class = RegisterArtistSerializer
#     # permission_classes = [Is_anybody,]
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()
#         refresh = RefreshToken.for_user(user)
#         res = {
#             "refresh": str(refresh),
#             "access": str(refresh.access_token),
#         }

#         return Response({
#             "user": serializer.data,
#             "refresh": res["refresh"],
#             "token": res["access"]
#         }, status=status.HTTP_201_CREATED)




class SignUpArtistView(generics.CreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = RegisterArtistSerializer

class SignUpCustomerView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = RegisterCustomerSerializer

class SignUpExpertView(generics.CreateAPIView):
    queryset = Expert.objects.all()
    serializer_class = RegisterExpertSerializer





class RegisterExpertAPI(generics.GenericAPIView):
    serializer_class = RegisterExpertSerializer
    # permission_classes = [Is_anybody,]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)


class RegisterCustomerAPI(generics.GenericAPIView):
    serializer_class = RegisterCustomerSerializer
    # permission_classes = [Is_anybody,]
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        res = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

        return Response({
            "user": serializer.data,
            "refresh": res["refresh"],
            "token": res["access"]
        }, status=status.HTTP_201_CREATED)






class LogInAPI(generics.GenericAPIView):
    serializer_class = LogInSerializer


# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginSerializers

#     def post(self, request):


#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data

#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]})



class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginSerializers
    # permission_classes = [Is_anybody,]

    def post(self, request):


        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data

        







        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]})



# class LogInAPI(TokenObtainPairView):
#     serializer_class = LogInSerializer
    
    # serializer_class = LoginSerializers
    # http_method_names = ['get', 'head', 'post']
    # # permission_classes = [Is_anybody,]
    # def post(self, request):
    #     self.http_method_names.append("GET")

    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.validated_data





        
    #     return Response({
    #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
    #         "token": AuthToken.objects.create(user)[1]})

# class LogInView(generics.GenericAPIView): # new
#     serializer_class = LogInSerializer

#     def post(self , request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": AuthToken.objects.create(user)[1]})



class Get_artist(generics.GenericAPIView):

    def get(self, request , pk):

        req = request.data
        artist = Artist.objects.get(national_id_number=pk)
        serializer = ArtistSerializer(artist, many=False)
        return Response(serializer.data)




class Get_expert(generics.GenericAPIView):

    def get(self, request , pk):

        req = request.data
        expert = Expert.objects.get(national_id_number=pk)
        serializer = ExpertSerializer(expert, many=False)
        return Response(serializer.data)

class Get_customer(generics.GenericAPIView):

    def get(self, request , pk):

        req = request.data
        customer = Customer.objects.get(national_id_number=pk)
        serializer = CustomerSerializer(customer, many=False)
        return Response(serializer.data)



class Get_artist_with_token(generics.GenericAPIView):
    serializer_class = ArtistSerializer
    def get(self, request , pk):

        artist = AuthToken.objects.get(digest=pk)
        test_user = artist.user
        # print (test_user)
        retUser = Artist.objects.get(user=test_user)
        serializer = ArtistSerializer(retUser, many=False)
        return Response(serializer.data)


class Get_expert_with_token(generics.GenericAPIView):
    serializer_class = ArtistSerializer
    def get(self, request , pk):

        expert = AuthToken.objects.get(digest=pk)
        test_user = expert.user
        # print (test_user)
        retUser = Expert.objects.get(user=test_user)
        serializer = ExpertSerializer(retUser, many=False)
        return Response(serializer.data)




class Get_customer_with_token(generics.GenericAPIView):
    serializer_class = ArtistSerializer
    def get(self, request , pk):

        customer = AuthToken.objects.get(digest=pk)
        test_user = customer.user
        # print (test_user)
        retUser = Customer.objects.get(user=test_user)
        serializer = CustomerSerializer(retUser, many=False)
        return Response(serializer.data)