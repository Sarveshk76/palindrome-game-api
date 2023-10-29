from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Game
from .serializers import GameSerializer
import random
import string
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework.permissions import IsAuthenticated


class GameListAPIView(ListAPIView):
    """Game List API View"""
    permission_classes = (IsAuthenticated,)
    queryset = Game.objects.all()
    serializer_class = GameSerializer

class GameCrudAPIView(APIView):
    """Game CRUD API View"""
    permission_classes = (IsAuthenticated,)
    
    @extend_schema(
        description="Create a new game",
        request=OpenApiTypes.OBJECT,
        responses={201: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                "Create a new game",
                summary="Create a new game",
                description="Post blank data to create a new game",
                value={
                    
                },
            ),
        ],
    )

    def post(self, request):
        game = Game.objects.create(user=self.request.user,
                                string="")
        game.save()
        return Response({'message': 'Game created',
                         'game': game.id,
                         'user': game.user.username})
    
    @extend_schema(
        description="Retrieve a game",
        request=OpenApiTypes.OBJECT,
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                "Retrieve a game",
                summary="Retrieve a game",
                description="Retrieve a game",
                value={
                    
                },
            ),
        ],
    )
    
    def get(self, request):
        try:
            game = Game.objects.filter(user=self.request.user).order_by('-id')[0]
            print(game)
            return Response({'message': 'Game retrieved',
                             'user': game.user.username,
                             "game": {"id": game.id,'string': game.string,}})
        except:
            return Response({'message': 'Game does not exist'})
    
    @extend_schema(
        description="Update a game",
        request=OpenApiTypes.OBJECT,
        responses={200: OpenApiTypes.OBJECT},
        examples=[
            OpenApiExample(
                "Update a game",
                summary="Update a game",
                description="Update a game",
                value={
                    "char": "a"
                },
            ),
        ],
    )

    def put(self, request):
        try:
            letters = string.ascii_lowercase
            random_char = random.choice(letters)

            game = Game.objects.filter(user=self.request.user).last()
            if len(game.string) <6:
                if len(request.data['char']) > 1 or len(request.data['char']) == 0 or request.data['char'].isalpha() == False:
                    return Response({'message': 'Invalid input, please enter a single character'})
                if request.data['char'].isalpha() == True and len(request.data['char']) == 1:
                    game.string += request.data['char']+random_char
                game.save()
                return Response({'message': 'Game updated', 'game': game.id, 'string': game.string})
            elif len(game.string) == 6:
                if game.string == game.string[::-1]:
                    game.is_palindrome = True
                    game.save()
                    return Response({'message': 'string is a palindrome, game over!!'})
                else:
                    return Response({'message': 'string is not a palindrome, game over!!'})
            else:
                return Response({'message': 'string length is already 6, game over!!'})
        except:
            return Response({'message': 'Game does not exist'})