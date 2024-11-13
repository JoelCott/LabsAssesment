# --// Scientific Calculator \\--

# --// Vairables & Services \\--
import math
import time
List1 = []
Quit = 'n'
while Quit != 'y':
# --// Functions, Procedures & Paramaters \\--
    def mainQuestion():
        for i in range(0,len(List1)):
            List1.pop()
        for i in range(0,listSize):
            userInput = int(input("Please now enter the numbers you would like to calculate: "))
            List1.append(userInput)
        print("Your current list: ",List1)
        
    def add(List1):
        global userInput
        global Quit
        numbers1 = len(List1)
        sum = 0
        sum = int(sum)

        for i in range(0,numbers1):
            sum = sum + List1[i]
        print(f"Sum of the array elements is: {sum}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()

    def sub(List1):
        global userInput
        global Quit
        numbers1 = len(List1)
        subt = 0
        subt = int(List1[0])

        for i in range(1,numbers1):
            subt = subt - List1[i]
            # print(f"TEST {subt}")
        print(f"The subtraction of the array elements is: {subt}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
            
    def multiply(List1):
        global userInput
        global Quit
        numbers1 = len(List1)
        multi = 0
        multi = int(List1[0])

        for i in range(1,numbers1):
            multi = multi * List1[i]
           # print(f"TEST {multi}")
        print(f"The multiplication of the array elements is: {multi}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
            
    def division(List1):
        global userInput
        global Quit
        numbers1 = len(List1)
        div = 0
        div = int(List1[0])

        for i in range(1,numbers1):
            if div == 0 or div == "0"  or List1[i] == 0:
                print("ERROR - You cannot divide a digit by ZERO. Please try again.")
                for i in range(0,numbers1):
                    List1.pop()
                print("The values you have entered have been cleared please enter new numbers.")
                mainQuestion()
            else:
                div = div // List1[i]
                    
            #print(f"TEST {div}")
        print(f"The division of the array elements is: {div}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
                  
    def squareRoot(List1):
        global Quit
        global i 
        numbers1 = len(List1)
        for i in range(0,numbers1):
            x = math.sqrt(List1[i])
            i += 1
            x = int(x)
            print(f"The square root of your number(s) are {x}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
            
    def trig(List1):
        angleDegree = List1[0]
        angleRadius = math.radians(angleDegree)
        sinValue = round(math.sin(angleRadius),5)
        cosValue = round(math.cos(angleRadius),5)
        tanValue = round(math.tan(angleRadius),5)
        
        print(f"Sin{angleDegree} = {sinValue} \n Cos{angleDegree} = {cosValue} \n Tan{angleDegree} = {tanValue}")
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
            
    def log(List1):
        global Quit
        numbers1 = len(List1)
        logg = int(List1[0])

        for i in range(1,numbers1):
            print("Logarithm for number: ",List1[i], math.log(List1[i]))
            logg += 1
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
    
    def expo(List1):
        numbers1 = len(List1)
        expoo = int(List1[0])

        for i in range(1,numbers1):
            print("Exponential for number: ",List1[i], math.log(List1[i]))
            expoo += 1
        firstQuestion = input("Would you like to continue using the program? 'y' or 'n'").lower()
        if firstQuestion == "n":
            print("Closing the program. Please wait..")
            time.sleep(2)
            print("Successfully closed.")
            Quit = "y"
            quit()
        else:
            print("Continuing the program")
            mainQuestion()
        

    

# --// Main Code \\--
    print("****---Welcome to the calculator---****")
    print("\n")
    print("Enter a MAXIMUM of 1 number if you decide to use the trigonomotry option. This is for the angle degree to work out the trigonometry of the value.")
    time.sleep(3)
    listSize = int(input("Please the amount of numbers you would like to use in your calculation: "))
    mainQuestion()
    
    print("Please read the following instructions carefully Please enter a number corresponding to the function you would like to run. \n 1 - Addition \n 2 - Subtraction \n 3 - Multiplication \n 4 - Division \n 5 - Square Root \n 6 - Trigonometry \n 7 - Logarithm \n 8 - Exponential")
    time.sleep(.2)

    secondQuestion = input("Please now enter the number corresponding to the function you want to use: ")

        
    if secondQuestion == "1":
        print("Loading Addition.")
        add(List1)      
    elif secondQuestion == "2":
        print("Loading Subtraction")
        sub(List1)
    elif secondQuestion == "3":
        print("Loading Multiplication")
        multiply(List1)
    elif secondQuestion == "4":
        print("Loading Division")
        division(List1)
    elif secondQuestion == "5":
        print("Loading Square Root")
        squareRoot(List1)
    elif secondQuestion == "6":
        print("Loading Trigonometry")
        trig(List1)
    elif secondQuestion == "7":
        print("Loading Logarithm")
        log(List1)
    elif secondQuestion == "8":
        print("Loading Exponential")
        expo(List1)

    else:
        print("ERROR - The number you have entered has not been registered. Please try again.")
        mainQuestion()

    

