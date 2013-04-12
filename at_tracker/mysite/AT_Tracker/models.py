from django.db import models
import sys


class school(models.Model):
    Name = models.CharField("Name of School", max_length=50)
    City = models.CharField("City", max_length=50)

    def __unicode__(self):  # this names the variable for the admin site
        Unique = self.Name+self.City
        return Unique


class user(models.Model):
    Username = models.CharField("Username", max_length=50)
    Password = models.CharField("Password", max_length=50)
    School = models.ForeignKey(schools)

    def __unicode__(self):  # this names the variable for the admin site
        return self.Username


class grade(models.Model):
    Grade_Level = models.IntegerField()
    School = models.ForeignKey(school)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.Grade_Level+self.School
        return Unique_Name	


class student(models.Model):
    First_Name = models.CharField("First Name", max_length=50)
    Last_Name = models.CharField("Last Name", max_length=50)
    Middle_Name = models.CharField("Middle Name", max_length=50)
    School = models.ForeignKey(school)
    Grade = models.ForeignKey(grade)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.First_Name+self.Last_Name+self.School+self.Grade
        return Unique_Name


class teacher(models.Model):
    First_Name = models.CharField("First Name", max_length=50)
    Last_Name = models.CharField("Last Name", max_length=50)
    Middle_Name = models.CharField("Middle Name", max_length=50)
    School = models.ForeignKey(school)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.First_Name+self.Last_Name+self.Middle_Name+self.School
        return Unique_Name


class class(models.Model):
    Name = models.CharField("Name of Class", max_length=50)
    Grade = models.ForeignKey(grade)
    School = models.ForeignKey(schools)
    Teachers = models.ManyToManyField(teacher)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.Name+self.School
        return Unique_Name
