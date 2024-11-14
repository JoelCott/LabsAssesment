# --// Scientific Calculator \\--

# --// Vairables & Services \\--

import math # Importing the math library so that I can use the functions for the complex equations for the calculator
import time # Importing the time library so that I can use its functions to pause the program when required.
List1 = [] # Initialising the list for the inputted numbers to be stored in before calculations.
Quit = 'n' # Vairable storing n to break the loop once asked.
while Quit != 'y': # Looping the whole program until quit does not equal 'y'.
    
# --// Functions, Procedures & Paramaters \\--

    def mainQuestion(): # Setting the mainQuestion function
        for i in range(0,len(List1)): # Checking if the list contains any unwanted numbers.
            List1.pop() # Removing all numbers from the list so the program can restart.
        for i in range(0,listSize): # Looping the userInput based on how many numbers the user wants to enter.
            userInput = int(input("Please now enter the numbers you would like to calculate: ")) # Asking for the numbers to be entered that the user wants to calculate.
            List1.append(userInput) # Adding the given numbers to the list.
        print("Your current list: ",List1) # Outputting the list to the user to see what they have in their list.
        
    def add(List1): # Defining the add function and using it with the List1
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        sum = 0 # Creating sum vairable and setting the value to 0, this will be changed.
        sum = int(sum) # Casting the vairable to a integer from a string.

        for i in range(0,numbers1): # checking how many numbers are stored in the list.
            sum = sum + List1[i] # adding all the numbers together based what is in the list.
        print(f"Sum of the array elements is: {sum}") #outputting the addition of the all elements in the list.
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.

    def sub(List1): # Defining the subtraction function and using it with list1.
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        subt = 0 # Creating the subtract vairable and setting the value to 0.
        subt = int(List1[0]) # Casting the first position in the list to an integer

        for i in range(1,numbers1): # Checking how many numbers are stored in the list
            subt = subt - List1[i] # Subtracting all the numbers from eachother based on what numbers are in the list
            # print(f"TEST {subt}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
            
    def multiply(List1):
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        multi = 0 # Initialising the multiply vairable and setting it to 0
        multi = int(List1[0]) # Casting the string to an integer so that the calculation will work

        for i in range(1,numbers1): # Checking how many numbers are stored in the list
            multi = multi * List1[i] # multiplying all numbers in the list together.
           # print(f"TEST {multi}")
        print(f"The multiplication of the array elements is: {multi}") # Outputting the results of the calculation to the users.
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
            
    def division(List1): # Initialising the divison function
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        div = 0 # Creating the division vairable and setting it to 0
        div = int(List1[0]) # Casting the string to an integer so that the program will calculate the numbers correctly.

        for i in range(1,numbers1): # Checking the numbers in the list
            if div == 0 or div == "0"  or List1[i] == 0: # If the list contains the number 0, this code will catch the error
                print("ERROR - You cannot divide a digit by ZERO. Please try again.") # Telling the user that they cannot divide by 0
                for i in range(0,numbers1): # removing all numbers from the list to try divide again without the number 0
                    List1.pop() # clearing the numbers
                print("The values you have entered have been cleared please enter new numbers.") # \telling the user to try again
                mainQuestion() # Reloading the program
            else: # If the list does not contain the number 0, the program will continue.
                div = div // List1[i] # Dividing all numbers in the list by eachother
                    
            #print(f"TEST {div}")
        print(f"The division of the array elements is: {div}") # printing out the results
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
                  
    def squareRoot(List1): # initialising the squreRoot function
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        for i in range(0,numbers1): # Checking the amount numbers in the list
            x = math.sqrt(List1[i]) # Finding the square root of the mnumbers in the list
            i += 1 # adding 1 to index so that all numbers in the list will run through this function
            x = int(x) # casting the numbers to integer before storing back in the list
            print(f"The square root of your number(s) are {x}") # outputting results to the user
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
            
    def trig(List1): # initialisng the trigonometry function
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        angleDegree = List1[0] # Setting the angle to the number in the list
        angleRadius = math.radians(angleDegree) # calculating the radius of the angle
        sinValue = round(math.sin(angleRadius),5) # calculating the sin of the angle
        cosValue = round(math.cos(angleRadius),5) # calculating the cos of the angle
        tanValue = round(math.tan(angleRadius),5) # calculating the tan of the angle
        
        print(f"Sin{angleDegree} = {sinValue} \n Cos{angleDegree} = {cosValue} \n Tan{angleDegree} = {tanValue}") # outputting the values
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
            
    def log(List1): # initialising the logarithm function
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        logg = int(List1[0]) # casting the string to an integer

        for i in range(1,numbers1): # checking how many numbers are in the list
            print("Logarithm for number: ",List1[i], math.log(List1[i])) # outputting the logarithm for all numbers in the list
            i += 1 # incrementing the index so that all numbers go through the function
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
    
    def expo(List1): # initialising the exponent function
        global userInput # Setting userInput to global so that it can be used in this paramater.
        global Quit # Setting the Quit vairable to global so that it can be accessed by this paramater to end the program
        numbers1 = len(List1) # Finding the length of the list, how many numbers are stored in it.
        expoo = int(List1[0]) # casting the string to an integer

        for i in range(1,numbers1): # checking the numbers int he list
            print("Exponential for number: ",List1[i], math.log(List1[i])) # printing the exponent of all numbers in the list
            i += 1 # incrementing the index so that all numbers go through the function
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower() # Asking user if they want to continue or quit the program
        if firstQuestion == "y": # Checking if the user input was "y", if so the program will quit
            print("Closing the program. Please wait..") # Telling the user that the program is about to stop running
            time.sleep(2) # Pausing the code whilst the program closes.
            print("Successfully closed.") # Closing the program.
            Quit = 'y' # Breaking the loop.
            quit() # Quitting the program.
        else: # If the user does not enter "y" then the program will continue.
            print("Continuing the program") # Telling the user that the program will continue.
            mainQuestion() # Restarting the program by calling the main/original function.
        

# --// Main Code \\--

    print("****---Welcome to the calculator---****") # welcoming the user to the program
    print("\n") # printing a space between the first print and the second
    print("Enter a MAXIMUM of 1 number if you decide to use the trigonomotry option. This is for the angle degree to work out the trigonometry of the value.") # listing rules with the trigonometry function
    time.sleep(3) # pausing the program for 3 seconds whilst the user reads the condition for the trigonometry function
    listSize = int(input("Please the amount of numbers you would like to use in your calculation: ")) # asking the user to enter a number so the program knows how many numbers they want to pass into the function
    mainQuestion() # running the main function so that the user can then input the numbers of their choice into the list
    
    print("Please read the following instructions carefully Please enter a number corresponding to the function you would like to run. \n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n 5 - Square Root \n 6 - Trigonometry \n 7 - Logarithm \n 8 - Exponential") # telling the user the different options of functions they can choose from
    time.sleep(.2) # pausing the program so that the user can think about which calculation they want to do

    secondQuestion = input("Please now enter the number corresponding to the function you want to use: ") # asking the user to enter their choice of function to use

        
    if secondQuestion == "1": # checking that the user has asked for addition
        print("Loading Addition.") # telling the user that the addition function is running
        add(List1) # running the addition function with the values stored in the list
    elif secondQuestion == "2": # checking that the user has asked for subtraction
        print("Loading Subtraction") # telling the user that the subtraction function is running
        sub(List1) # running the subtraction function with the values stored in the list
    elif secondQuestion == "3": # checking that the user has asked for multiplication
        print("Loading Multiplication") # telling the user has asked for multiplication
        multiply(List1) # running the multiplication function with the values stored in the list
    elif secondQuestion == "4": # checking that the user has asked for divison
        print("Loading Division") # telling the user that the division function is running
        division(List1) # running the divison function with the numbers stored in the list
    elif secondQuestion == "5": # checking that the user has asked for square root
        print("Loading Square Root") # telling the user that the square root function is running
        squareRoot(List1) # running the square root function with the values stored in the list
    elif secondQuestion == "6": # checking that the user has asked for trigonometry
        print("Loading Trigonometry") # telling the user that the addition function is running
        trig(List1) # running the trigonometry function with the values stored in the list
    elif secondQuestion == "7": # checking that the user has asked for logarithm
        print("Loading Logarithm") # telling the user that the logarithm function is running
        log(List1) # running the logarithm function with the values stored in the list
    elif secondQuestion == "8": # checking that the user has asked for exponential
        print("Loading Exponential") # telling the user that the subtraction function is running
        expo(List1) # running the exponential function with the values stored in the list

    else: # if a incorrect value was entered the error will be catched by the statement below.
        print("ERROR - The number you have entered has not been registered. Please try again.") # telling the user that their input was not valid
        mainQuestion() # restarting the program