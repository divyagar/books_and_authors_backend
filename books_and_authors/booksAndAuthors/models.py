from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    price = models.IntegerField(null=False, blank=False)
    author = models.ForeignKey(Author, null=False, blank=False, on_delete=models.CASCADE) 

    def __str__(self) -> str:
        return self.name

