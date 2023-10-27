from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game
import random
import string


class GameCrudAPIView(APIView):
    
    def post(self, request):
        game = Game.objects.create(user=self.request.user, string="")
        game.save()
        return Response({'message': 'Game created',
                         'game': game.id,
                         'user': game.user.username})
    
    def get(self, request):
        try:
            game = Game.objects.filter(user=self.request.user).order_by('-id')[0]
            print(game)
            return Response({'message': 'Game retrieved',
                             'user': game.user.username,
                             "game": {"id": game.id,'string': game.string,}})
        except:
            return Response({'message': 'Game does not exist'})
    
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
            else:
                return Response({'message': 'string length is greater than 6, game over!!'})
        except:
            return Response({'message': 'Game does not exist'})