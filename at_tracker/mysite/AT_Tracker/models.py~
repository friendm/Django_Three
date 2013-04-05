from django.db import models

class Schools(models.Model):
	Name = models.CharField("Name of School", max_length = 50)
	City = models.CharField("City", max_length = 50)
		
	def __unicode__(self): #this names the variable for the admin site
		Unique =self.Name+self.City 
		return Unique
	
	def is_unique(self,Name,City):
		Name_List = models.Schools.objects.values('Name').distinct()
		City_List = models.Schools.objects.values('City').distinct()
		
		if Name_List.index(Name)==True & City_List.index(City)==True:
			return False
		else:
			return True
			
		
			

class Users(models.Model):
	Username = models.CharField("Username", max_length = 50)
	Password = models.CharField("Password", max_length = 50)
	School = models.ForeignKey(Schools)
	
	def __unicode__(self): #this names the variable for the admin site
		return self.Username

class Grade(models.Model):
	Grade_Level = models.IntegerField()
	School = models.ForeignKey(Schools)
		
	def __unicode__(self): #this names the variable for the admin site
		Unique_Name = self.Grade_Level+self.School
		return Unique_Name		
				

class Students(models.Model):
	First_Name = models.CharField("First Name" , max_length = 50 )
	Last_Name = models.CharField("Last Name" , max_length = 50 )
	Middle_Name = models.CharField("Middle Name" , max_length = 50 )
	School = models.ForeignKey(Schools)
	Grade = models.ForeignKey(Grade)
		
	def __unicode__(self): #this names the variable for the admin site
		Unique_Name = self.First_Name+self.Last_Name+self.School+self.Grade
		return Unique_Name		
				

class Teacher(models.Model):
	First_Name = models.CharField("First Name" , max_length = 50 )
	Last_Name = models.CharField("Last Name" , max_length = 50 )
	Middle_Name = models.CharField("Middle Name" , max_length = 50 )
	School = models.ForeignKey(Schools)

	def __unicode__(self): #this names the variable for the admin site
		Unique_Name = self.First_Name+self.Last_Name+self.Middle_Name+self.School
		return Unique_Name	

class Classes(models.Model):
	Name = models.CharField("Name of Class", max_length = 50)
	Grade = models.ForeignKey(Grade)
	School = models.ForeignKey(Schools)
	Teachers = models.ManyToManyField(Teacher)
		
	def __unicode__(self): #this names the variable for the admin site
		Unique_Name = self.Name+self.School
		return Unique_Name	
	
