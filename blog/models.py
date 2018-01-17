from django.db import models
from django.contrib.auth.models import User
import uuid

class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()
    # id = models.IntegerField(primary_key=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200,primary_key=True)
    email = models.EmailField()
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline


class City(models.Model):
    city_name = models.CharField(max_length=100)
    city_pop = models.IntegerField()

    def __str__(self):
        return self.city_name


class Branch(models.Model):
    city = models.ForeignKey(City, blank=True, null=True)
    branch_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()

    def __str__(self):
        return self.branch_name


class Employee(models.Model):
    emp_no = models.IntegerField()
    name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    salary = models.IntegerField()
    dob = models.DateField()
    hiredate = models.DateField()
    mgrno = models.IntegerField()
    gender = models.IntegerField(help_text='1 for male and 2 for female')
    city = models.ForeignKey(City, blank=True, null=True)
    deptno = models.IntegerField()

    def __str__(self):
        return self.name