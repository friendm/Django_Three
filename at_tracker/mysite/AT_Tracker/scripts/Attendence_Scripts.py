#the code in quotes is placeholder for pulling data from the database
"""
pull database data
"""

test_data=(0,1,0,1,1,0,0,0,0,0,0,0,1)

def Total_Days_Out(x):#Total Days Missed
    Count=0
    for items in x:
        if items==0:
            Count=Count+1
    print Count


def Days_In_Row(x):#Most Days in a Row Missed
    Count_Max=0
    Count_Temp=0
    for items in x:
        if items==0:
            Count_Temp+=1
	    if Count_Temp>Count_Max:
                Count_Max=Count_Temp
        else:
            Count_Temp=0
    print Count_Max


def Truancy_Percent(x):#Percentage of Range of Days in School
    Count=0
    Days=0
    for item in x:
        Days=Days+1
        if item==1:
            Count=Count+1
    Percent = float(Count)/Days
    print Percent

def Weekday_Most_Missed(x,y)#x is data,y is day range started on
    Monday=(1,5,4,3,2)
    Tuesday=(2,1,5,4,3)
    Wedensday=(3,2,1,5,4)
    Thursday=(4,3,2,1,5)
    Friday=(5,4,3,2,1)
    #accounts for change of start of day range
    Mon=0
    Tue=0
    Wed=0
    Thurs=0
    Fri=0
    count=0
    for item in x:
        count+=1
        if count%Monday[y-1]:
           Mon+=1
#repeat else if statment for 
        



        
Total_Days_Out(test_data)
Days_In_Row(test_data)
Truancy_Percent(test_data)


        

