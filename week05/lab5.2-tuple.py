# this program stores the months of the year in a tuple
# then creates a new tuple with summer months
# Author: Sarah McNelis

months = ("January", 
            "February", 
            "March", 
            "April", 
            "May", 
            "June", 
            "July",
            "August",
            "September",
            "October",
            "November",
            "December" 
)
summer = months[4:7]
# selecting element 4 up to but not including 7

for month in summer:
    print (month)