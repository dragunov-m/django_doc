from datetime import datetime
from django.utils import timezone
from django.db import models


# One - to - one
class User(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    #def __str__(self):
        #return f'User: {self.user.name} / Login: {self.login}'
# End One - to - one


# One - to - many
class Company(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return f'Vendor: {self.company.name} / Product Name: {self.name} / Price: {self.price}'
# End One - to - many


# Many - to - many
class Course(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
# End Many - to - many


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
