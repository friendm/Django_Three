from django.db import models

class Schools(models.Model):
	Name = models.CharField("Name of School", max_length = 50)
	City = models.CharField("City", max_length = 50)

class Users(models.Model):
	Username = models.CharField("Username", max_length = 50)
	Password = models.CharField("Password", max_length = 50)
	School = models.ForeignKey(Schools)

class Grade(models.Model):
		Grade_Level=models.IntegerField()
		School = models.ForeignKey(Schools)
	

class Students(models.Model):
	First_Name=models.CharField("First Name" , max_length = 50 )
	Last_Name=models.CharField("Last Name" , max_length = 50 )
	Middle_Name=models.CharField("Middle Name" , max_length = 50 )
	School = models.ForeignKey(Schools)
	Grade = models.ForeignKey(Grade)


class Teacher(models.Model):
		First_Name=models.CharField("First Name" , max_length = 50 )
		Last_Name=models.CharField("Last Name" , max_length = 50 )
		Middle_Name=models.CharField("Middle Name" , max_length = 50 )
		School = models.ForeignKey(Schools)



class Classes(models.Model):
		Name = models.CharField("Name of Class", max_length = 50)
		Grade= models.ForeignKey(Grade)
		School = models.ForeignKey(Schools)
		Teachers = models.ManyToManyField(Teacher)
		
		
	
