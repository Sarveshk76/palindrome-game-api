from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.permissions import IsAuthenticated


class UserCrudAPIView(APIView):
    """User CRUD API View"""
    permission_classes = (IsAuthenticated,)

    #create extended schema for swagger of post, put and delete methods
    @extend_schema(
        description="Create a new user",
        request=OpenApiTypes.OBJECT,
        responses={201: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                "Create a new user",
                summary="Create a new user",
                description="Create a new user",
                value={
                    "username": "testuser",
                    "password": "testpassword",
                    "email": "test@email.com",
                    "first_name": "test",
                    "last_name": "user"
                },
            ),
        ],
    )
    
    def post(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            email = request.POST.get('email')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')

            user, created = User.objects.get_or_create(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            if created:
                user.save()
                token = Token.objects.create(user=user)
                return Response({'message': 'User created', 'user': user.username, 'token': token.key})
            else:
                return Response({'message': 'User already exists'})
        except:
            return Response({'message': 'Invalid data'})

    @extend_schema(
        description="Update a user",
        request=OpenApiTypes.OBJECT,
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                "Update a user",
                summary="Update a user",
                description="Update a user",
                value={
                    "username": "testuser",
                    "first_name": "test",
                    "last_name": "user",
                    "email": "test@email.com"
                },
            ),
        ],
    )    
        
    def put(self, request):
        username = request.data['username']
        print(request.data)

        user = User.objects.get(username=username)
        if user is None:
            return Response({'message': 'User does not exist'})
        else:
            flag = 0
            if(all(x in request.data.keys() for x in ['first_name', 'last_name', 'email'])):
                flag = 1
            if flag:
                if request.POST.get('first_name'):
                    user.first_name = request.POST.get('first_name')
                if request.POST.get('last_name'):
                    user.last_name = request.POST.get('last_name')
                if request.POST.get('email'):
                    user.email = request.POST.get('email')
                user.save()
                return Response({'message': 'User updated', 'user': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
            else:
                return Response({'message': 'No data to update', 'user': user.username, 'first_name': user.first_name, 'last_name': user.last_name, 'email': user.email})
    
    @extend_schema(
        description="Delete a user",
        request=OpenApiTypes.OBJECT,
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                "Delete a user",
                summary="Delete a user",
                description="Delete a user",
                value={
                    "username": "testuser"
                },
            ),
        ],
    )
    
    def delete(self, request):
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        if user is None:
            return Response({'message': 'User does not exist'})
        else:
            user.delete()
            return Response({'message': 'User deleted'})