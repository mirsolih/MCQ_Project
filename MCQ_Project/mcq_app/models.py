from django.db import models
from django .contrib.auth.models import User


# Create your models here.
class Category(models. Model):
    title = models.CharField(max_length=2, null = True)
    topic = models.CharField(max_length=100, null = True)
    def __str__(self): 
        return self.topic  
    
class Question(models. Model):
    category = models.ForeignKey(Category, null = True, on_delete=models.CASCADE)
    text = models.TextField(null = True) 
    def __str__(self): 
        return self.text
    
class Answer(models.Model):
    question = models.ForeignKey(Question, null = True, on_delete = models.CASCADE)
    a = models.CharField(max_length = 100, null = True)
    b = models.CharField(max_length = 100, null = True)
    c = models.CharField(max_length = 100, null = True)
    correct = models.CharField(max_length = 100, null = True)
    
    

class Everything(models.Model):
    category = models.ForeignKey(Category, null = True, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, null = True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null = True, on_delete=models.CASCADE)

class Template(models.Model):
    name = models.CharField(max_length = 50, null = True)
    pass
    def __str__(self): 
        return self.name


class Cat_Amount(models.Model):
    template = models.ManyToManyField(Template)
    category = models.ForeignKey(Category, null = True, on_delete=models.CASCADE)
    quantity = models.IntegerField(null = True)

class Test(models.Model):
    template = models.ForeignKey(Template, null = True, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50, null = True)
    def __str__(self):
        return self.name 

    


 



