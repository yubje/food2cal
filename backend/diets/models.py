from django.db import models
from django.conf import settings

from posts.models import Post

class Diet:
    diet_image_path = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)



class Food:
    food_name = models.CharField(max_length=100)
    amount = models.IntegerField()
    calorie = models.IntegerField()
    carbyhydrate = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE)


class Nutrition:
    food_name = models.CharField()
    amount = models.IntegerField() 
    calorie = models.IntegerField() 
    carbohydrate = models.IntegerField() 
    protein = models.IntegerField() 
    fat = models.IntegerField() 

