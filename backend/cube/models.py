from django.db import models

class Rank(models.Model):
    username = models.CharField(max_length=255)
    time = models.DurationField()

    def __str__(self):
        return f'username: {self.username}, time: {self.time}'
    
    def __repr__(self):
        return self.__str__()
    
    def get_rank_position(self):
        return list(Rank.objects.all().order_by('time').values_list('id', flat=True)).index(self.id) + 1
