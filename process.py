#This line connects the python file the the um-server to gather the information
log_file = open("um-server-01.txt")

#This creates the a function
def sales_reports(log_file):
    #this creates a for loop 
    for line in log_file:
        #this returns a coyp to the variable line with any trailing characters removed
        line = line.rstrip()
        #this is singling out a postion from the line variable
        day = line[0:3]
        #this is an "if" statement returning the day asked for if the conditions are met
        if day == "Mon":
            #returning the conditions
            print(line)

#calling the function sales_report
sales_reports(log_file)
