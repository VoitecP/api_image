from gallery.models import *
from .serializers import *
from django.shortcuts import redirect, get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin

from rest_framework.pagination import PageNumberPagination
from rest_framework import status


class Paginator(PageNumberPagination):
    page_size=5
    page_size_query_param = 'page_size'
    max_page_size=10


class TokenView(APIView):
    def get(self, *args,**kwargs):                   #  first() prevents multi queryset error
        # queryset=UserImage.objects.get(**kwargs)      
        queryset=UserImage.objects.filter(**kwargs).first()
        response=Response()
        response['Token Link Validator']='Proparbly wrong link'
        try:
            return redirect(queryset.img.url)  
        except:
            return response

  
class DetailImageView(APIView):         # problem with passing request to serializer
    serializer_class=UserImageSerializer

    def get(self,request, pk, *args, **kwargs):
        queryset=UserImage.objects.filter(id=pk)
        serializer=UserImageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UploadUserImageView(APIView):
    serializer_class=UploadUserImageSerializer

    def get(self, request):
        queryset=UserImage.objects.none()
        return Response({"Upload": 'Image'})

    def post(self, request):
        serializer=UploadUserImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # queryset=UserImage.objects.filter(id=request.data["id"]).values()
            return serializer.data 
            # return Response({"Message":"New added", "List":serializer.data})


class UserImageGenericView(GenericAPIView,CreateModelMixin):
    serializer_class=UploadUserImageSerializer
    queryset=UserImage.objects.all()

    def perform_create(self, serializer):
        queryset=get_object_or_404(User, id=self.request.data.get('user'))
        return serializer.save(user=queryset)

    def post(self, serializer, request, *args, **kwargs):
        # return self.create(request, *args, **kwargs)
        return Response({"Successfuly send image":serializer.data})
        

class GalleryView(APIView, Paginator):
    serializer_class=UserImageSerializer

    def get(self,request,pk):
        queryset=UserImage.objects.filter(user__id=pk)
        page=self.paginate_queryset(queryset, request ,view=self)
        serializer=UserImageSerializer(page, many=True)
        response=self.get_paginated_response(serializer.data)
        return response
       

class APIUrls(APIView):
    """
    Add url endpoints to base view
    """
    def get(self,request):
        data={
            "Root                           ": "http://127.0.0.1:8000/api/",
            "Admin Panel,                   ": "http://127.0.0.1:8000/api/admin/", 
            "":"",
            "Upload Image Endpoint          ": "http://127.0.0.1:8000/api/userimage/",
            "Image Detail View              ":"http://127.0.0.1:8000/api/userimage/1/",
            # "Upload Image Endpoint, generic ": "http://127.0.0.1:8000/api/generic/userimage/1",
            "User's Gallery, paginated      ": "http://127.0.0.1:8000/api/gallery/1/",
            "Example Endpoint for Token     ": "http://127.0.0.1:8000/api/token/<hash>",
            ".":".",
            "Below List of Api Endpoint generated by Router, and Nested Router": "",
            ".":".",
            "Api v2 Routed                  ":"http://127.0.0.1:8000/api/v2/",
        }

        return Response(data)


    
       