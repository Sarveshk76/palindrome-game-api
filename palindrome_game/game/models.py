from django.db import models

class Game(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='game')
    string = models.CharField(max_length=6)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username