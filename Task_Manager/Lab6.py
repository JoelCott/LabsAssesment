#--// Vairables & Services

flag = False

# --// Dictionaries & Lists \\--
days_of_week = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}
 
task_MonthsofYear = {
    "January": [],
    "February": [],
    "March": [],   
    "April": [],
    "May": [],
    "June": [],
    "July": [],
    "August": [],
    "September": [],
    "October": [],
    "November": [],
    "December": [],
}
 
 # --// Functions, Procedures & Paramaters
 
def addTask_day(day, task):
    if day in days_of_week:
        days_of_week[day].append(task)
    else:
        print("ERROR - Input not Validated")
 
def addTask_month(month, task):
    if month in task_MonthsofYear:
        task_MonthsofYear[month].append(task)
    else:
        print("ERROR - Input not Validated")

 
def removeTask_day(day, task):
    if day in days_of_week:
        if task in days_of_week[day]:
            days_of_week[day].remove(task)
        else:
            print("ERROR - Task could not be located.")
    else:
        print("ERROR - Input not Validated")
 
def removeTasks_month(month, task):
    if month in task_MonthsofYear:
        if task in task_MonthsofYear[month]:
            task_MonthsofYear[month].remove(task)
        else:
            print("ERROR - Task could not be located.")
    else:
        print("ERROR - Input not Validated")
 
def viewTask_day(day):
    if day in days_of_week:
        print(f"{day} tasks: {days_of_week[day]}")
    else:
        print("ERROR - Input not Validated")
 
def viewTask_month(month):
    if month in task_MonthsofYear:
        print(f"{month} tasks: {task_MonthsofYear[month]}")
    else:
        print("ERROR - Input not Validated")
 
def addTask_month(month, task):
    if month in task_MonthsofYear:
        task_MonthsofYear[month].append(task)
    else:
        print("ERROR - Input not Validated")
 
def viewTask_month(month):
    if month in task_MonthsofYear:
        print(f"{month} tasks: {task_MonthsofYear[month]}")
    else:
        print("ERROR - Input not Validated")
 
# --// Main Code \\--

while True:
    flag = True
    print("----**** Welcome to the Task Manager ****----")
    print("Please read the following instructions carefully and choose what you'd like to do: \n 1 - Add a task to a specific day or month \n 2 - Remove a task from a specific day or month \n 3 - View the current tasks in a day or month \n 4 - Quit the program ")
    mainQuestion = input("Enter '1', '2', '3', or '4' now: ")
    secondQuestion = input("Please now choose 'Day' or 'Month' to use the previous action on: ").capitalize()
    if secondQuestion == "Day":
        if mainQuestion == "4":
            flag == True
            #quit()
            break
        elif mainQuestion == "1":
            day = input("Enter the day of the week: ").capitalize()
            task = input("Enter the task: ")
            addTask_day(day, task)

        elif mainQuestion == "2":
            day = input("Enter the day of the week: ").capitalize()
            task = input("Enter the task: ")
            removeTask_day(day, task)
            flag = False

        elif mainQuestion == "3":
            day = input("Enter the day of the week: ").capitalize()
            viewTask_day(day)
            flag = False

        else:
            print("ERROR - Input not Validated")
            flag = False
            
    elif secondQuestion == "Month":
        if mainQuestion == "4":
            flag == True
            quit()
        elif mainQuestion == "1":
            month = input("Enter a month of the year: ").capitalize()
            task = input("Enter the task: ")
            addTask_day(day, task)
            flag = False

        elif mainQuestion == "2":
            month = input("Enter a month of the year: ").capitalize()
            task = input("Enter the task: ")
            removeTask_day(day, task)
            flag = False

        elif mainQuestion == "3":
            month = input("Enter a month of the year: ").capitalize()
            viewTask_day(day)
            flag = False

        else:
            print("ERROR - Input not Validated")
            flag = False
    
 
