# --// Task Manager \\--

#--// Variables & Services

import time  # Importing the time module for sleep functionality
flag = False  # A flag variable, currently unused

# --// Dictionaries & Lists \\--

# Dictionary to hold tasks for each day of the week
days_of_week = {
    "Monday": [],
    "Tuesday": [],
    "Wednesday": [],
    "Thursday": [],
    "Friday": [],
    "Saturday": [],
    "Sunday": []
}
 
# Dictionary to hold tasks for each month of the year
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
 
# --// Functions, Procedures & Parameters
 
# Function to add a task to a specific day
def addTask_day(day, task):
    if day in days_of_week:  # Check if the day is valid
        days_of_week[day].append(task)  # Add the task to the days list
    else:
        print("ERROR - Input not Validated")  # Error message for invalid day
 
# Function to add a task to a specific month
def addTask_month(month, task):
    if month in task_MonthsofYear:  # Check if the month is valid
        task_MonthsofYear[month].append(task)  # Add the task to the months list
    else:
        print("ERROR - Input not Validated")  # Error message for invalid month

# Function to remove a task from a specific day
def removeTask_day(day, task):
    if day in days_of_week:  # Check if the day is valid
        if task in days_of_week[day]:  # Check if the task exists for that day
            days_of_week[day].remove(task)  # Remove the task from the days list
        else:
            print("ERROR - Task could not be located.")  # Error if task not found
    else:
        print("ERROR - Input not Validated")  # Error message for invalid day
 
# Function to remove a task from a specific month
def removeTasks_month(month, task):
    if month in task_MonthsofYear:  # Check if the month is valid
        if task in task_MonthsofYear[month]:  # Check if the task exists for that month
            task_MonthsofYear[month].remove(task)  # Remove the task from the months list
        else:
            print("ERROR - Task could not be located.")  # Error if task not found
    else:
        print("ERROR - Input not Validated")  # Error message for invalid month
 
# Function to view tasks for a specific day
def viewTask_day(day):
    if day in days_of_week:  # Check if the day is valid
        print(f"{day} tasks: {days_of_week[day]}")  # Print the tasks for that day
    else:
        print("ERROR - Input not Validated")  # Error message for invalid day
 
# Function to view tasks for a specific month
def viewTask_month(month):
    if month in task_MonthsofYear:  # Check if the month is valid
        print(f"{month} tasks: {task_MonthsofYear[month]}")  # Print the tasks for that month
    else:
        print("ERROR - Input not Validated")  # Error message for invalid month
 
# --// Main Code \\--

while True:  # Infinite loop to keep the program running until told to break, when the user decides to quit and when they are prompted
    print("----**** Welcome to the Task Manager ****----")  # Welcome message
    print("Please read the following instructions carefully and choose what you'd like to do: \n 1 - Add a task to a specific day or month \n 2 - Remove a task from a specific day or month \n 3 - View the current tasks in a day or month \n 4 - Quit the program ")
    
    mainQuestion = input("Enter '1', '2', '3', or '4' now: ")  # User input for main action
    
    if mainQuestion == "4":  # Check if the user wants to quit
        break  # Exit the loop immediately if the user wants to quit
    
    secondQuestion = input("Please now choose 'Day' or 'Month' to use the previous action on: ").capitalize()  # User input for day or month
    
    if secondQuestion == "Day":  # If the user chooses Day
        if mainQuestion == "1":  # If the user wants to add a task
            day = input("Enter the day of the week: ").capitalize()  # Get the day from user
            task = input("Enter the task: ")  # Get the task from user
            addTask_day(day, task)  # Call function to add task
            print("Your task has been added successfully")  # Confirmation message
            print("\n")
            time.sleep(2)  # Pause for 2 seconds
        elif mainQuestion == "2":  # If the user wants to remove a task
            day = input("Enter the day of the week: ").capitalize()  # Get the day from user
            task = input("Enter the task: ")  # Get the task from user
            removeTask_day(day, task)  # Call function to remove task
            print("Your task has been removed Successfully")  # Confirmation message
            print("\n")
            time.sleep(2)  # Pause for 2 seconds
        elif mainQuestion == "3":  # If the user wants to view tasks
            day = input("Enter the day of the week: ").capitalize()  # Get the day from user
            print(f"Your task for {day} is loading..")  # Loading message
            print("\n")
            viewTask_day(day)  # Call function to view tasks
            time.sleep(2)  # Pause for 2 seconds
        else:
            print("ERROR - Input not Validated")  # Error message for invalid input
            print("\n")
            
    elif secondQuestion == "Month":  # If the user chooses Month
        if mainQuestion == "1":  # If the user wants to add a task
            month = input("Enter a month of the year: ").capitalize()  # Get the month from user
            task = input("Enter the task: ")  # Get the task from user
            addTask_month(month, task)  # Call function to add task
            print("Your task has been added successfully.")  # Confirmation message
            print("\n")
            time.sleep(2)  # Pause for 2 seconds
        elif mainQuestion == "2":  # If the user wants to remove a task
            month = input("Enter a month of the year: ").capitalize()  # Get the month from user
            task = input("Enter the task: ")  # Get the task from user
            removeTasks_month(month, task)  # Call function to remove task
            print("Your task has been removed Successfully.")  # Confirmation message
            print("\n")
            time.sleep(2)  # Pause for 2 seconds
        elif mainQuestion == "3":  # If the user wants to view tasks
            month = input("Enter a month of the year: ").capitalize()  # Get the month from user
            print(f"Your task for {month} is loading..")  # Loading message
            print("\n")
            time.sleep(2)  # Pause for 2 seconds
            viewTask_month(month)  # Call function to view tasks
        else:
            print("ERROR - Input not Validated")  # Error message for invalid input