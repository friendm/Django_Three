from django.db import models
import sys



class school(models.Model):
    Name = models.CharField("Name of School", max_length=50)
    City = models.CharField("City", max_length=50)

    def __unicode__(self):  # this names the variable for the admin site
        Unique = self.Name + "--" + self.City
        return Unique


class user(models.Model):
    Username = models.CharField("Username", max_length=50)
    Password = models.CharField("Password", max_length=50)
    School = models.ForeignKey(school)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.Username + "--" + self.Password + "--"
        School = str(self.School)
        Unique_Name = Unique_Name + School
        return Unique_Name


class grade(models.Model):
    Grade_Level = models.IntegerField()
    School = models.ForeignKey(school)

    def __unicode__(self):  # this names the variable for the admin site
        Grade = str(self.Grade_Level)
        Schools = str(self.School)
        Unique_Name = Grade + "--" + Schools
        return Unique_Name	


class student(models.Model):
    First_Name = models.CharField("First Name", max_length=50)
    Last_Name = models.CharField("Last Name", max_length=50)
    Middle_Name = models.CharField("Middle Name", max_length=50)
    School = models.ForeignKey(school)
    Grade = models.ForeignKey(grade)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.First_Name + "--" + self.Middle_Name + "--"
        Unique_Name = Unique_Name + self.Last_Name
        return '%s %s %s %s %s' % (unicode(self.School), "--", Unique_Name, "--", unicode(self.Grade))


class teacher(models.Model):
    First_Name = models.CharField("First Name", max_length=50)
    Last_Name = models.CharField("Last Name", max_length=50)
    Middle_Name = models.CharField("Middle Name", max_length=50)
    School = models.ForeignKey(school)

    def __unicode__(self):  # this names the variable for the admin site
        return '%s %s %s %s %s' % (unicode(self.School), "--", self.First_Name, "--", self.Last_Name)
        # the foriegn key needs to be added with the unicode method
        # in order for Django to recognize it


class subject(models.Model):  
    Name = models.CharField("Name of Class", max_length=50)
    Grade = models.ForeignKey(grade)
    School = models.ForeignKey(school)
    Teachers = models.ManyToManyField(teacher)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.Name + "--" + self.School
        return Unique_Name
        

class attendence(models.Model):  
    Date = models.CharField("Date", max_length=50)
    Grade = models.ForeignKey(grade)
    School = models.ForeignKey(school)
    Subject = models.ForeignKey(subject)
    Student = models.ForeignKey(student)

    def __unicode__(self):  # this names the variable for the admin site
        Unique_Name = self.Date + "--" + self.Grade + "--" + self.Student
        return Unique_Name
        


