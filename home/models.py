from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Continent(models.Model):
    Name = models.CharField(max_length = 50)

    def __str__(self):
        return self.Name
    

class State(models.Model):
    IdContinents = models.ForeignKey(Continent, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name = "likes", blank = True)
    dislikes = models.ManyToManyField(User, related_name = "dislikes", blank = True)
    Name = models.CharField(max_length = 50)
    Flag = models.ImageField(default = "download.jpg",height_field="height_field", width_field="width_field",
     null = True , blank = True, upload_to='Flags')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return self.Name

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

kategorite = {
    ('Ekonomia','Ekonomia'),
    ('Turizmi', 'Turizmi'),
    ('Gjeografi','Gjeografi'),
    ('Klima','Klima'),
    ('Kulture','Kulture'),
}

class Categorie(models.Model):
    Name = models.CharField(max_length = 50, choices=kategorite, default="ekonomia")

    def __str__(self):
        return self.Name


class Information(models.Model):
    confirm = models.BooleanField(default=False)
    IdContinents = models.ForeignKey(Continent, on_delete=models.CASCADE)
    IdState = models.ForeignKey(State, on_delete=models.CASCADE)
    Flag = models.ImageField(default = "download.jpg",height_field="height_field", width_field="width_field",
     null = True , blank = True, upload_to='Flags')
    IdCategorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, default="ekonomia")
    Title = models.CharField(max_length = 50)
    Information = models.TextField(max_length = 1000)
    Photo = models.ImageField(default = "download.jpg", null = True , blank = True, upload_to='Photo')
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    def __str__(self):
        return str(self.IdState) + ", " + self.Title



