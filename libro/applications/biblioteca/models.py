from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField('Names',max_length=80)
    nationality = models.CharField(blank=True,max_length=100)

    #By default django will return name
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField('Titles', max_length=100)
    resume = models.TextField('Resume', blank=True)
    #Cascade= when I rm an author his books will be deleted as well
    author = models.ForeignKey(Author, on_delete=models.CASCADE) 

    #By default django will return title
    def __str__(self):
        return self.title