from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token



class UserCrudAPIView(APIView):

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
    
    def delete(self, request):
        username = request.POST.get('username')
        user = User.objects.get(username=username)
        if user is None:
            return Response({'message': 'User does not exist'})
        else:
            user.delete()
            return Response({'message': 'User deleted'})