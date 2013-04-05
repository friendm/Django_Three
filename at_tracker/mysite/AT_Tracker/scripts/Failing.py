Grades = []
Grades = [["A","B","C","D","F"],[4,3,2,1,0]]

Failing_Threshold = 2 #set threshold for failure here
Sports_Elig = 4 # set threshold for sports elegibility here

Student_One_Grades=["A","B","F","F","A","A"]  #list of student grades

GPA=0

for x in Student_One_Grades:
	GPA_Lookup = Grades[0].index(x)
	GPA += Grades[1][GPA_Lookup]
	
GPA = float(GPA)/len(Student_One_Grades)

Sports_Status = 0
Fail_Status = 0

if GPA < Failing_Threshold:
	 Fail_Status = "Student is failing"
else:
	Fail_Status = "Student is passing"
	
if GPA > Sports_Elig:
	 Sports_Status = "Student can play sports"
else:
	Sports_Status = "Student cannot play sports"

print Fail_Status + "--" + Sports_Status 	
