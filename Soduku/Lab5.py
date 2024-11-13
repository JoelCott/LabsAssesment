# --// Sudoku \\--

# --// Variables & Services \\--
import time
sGrid = []  # Initializing the list to store the numbers in for the grid.
flag = False # Setting the flag to False to ensure that the functions run first to create the grid before activating the loop

# --// Procedures Functions & Parameters \\--

# Creating the grid and filling it with 0s
def createGrid():
    global flag  # Declare flag as global so that it can be accessed and changed by the this procedure
    for i in range(9): # Creating the rows in the list
        row = [0] * 9  # Filling the row with 0s
        sGrid.append(row) # Applying the rows to the list to be appended on user input
    flag = True # Allowing the while loop to continously run

# Function to print the grid
def displayGrid():
    for row in sGrid: # Searching the list to find all the rows
        print(" ".join(map(str, row))) # Printing the list in a 9x9 format

# Check if the move is valid
def validateMove(row, column, num):
    if num in sGrid[row]:  # Checking row to see if it's full or not 
        print("ERROR - Row full") # Alerting the user that the row is full if there is an attempt to place a number in the row        
        return False # Returning no value as it is only a validation check
    
    if num in [sGrid[r][column] for r in range(9)]:  # Checking column to see if it's full or not
        print("ERROR - Column full") # Alerting the user that the column is full if there is an attempt to place a number in the column
        return False # Returning no value as it is only a validation check
    
    startRow, startColumn = 3 * (row // 3), 3 * (column // 3)  # Setting up how the user inputs the data by row, column, number
    for i in range(startRow, startRow + 3): # 
        for j in range(startColumn, startColumn + 3):
            if sGrid[i][j] == num:  # Checking the user input for duplicates
                print("ERROR - Duplicate found")
                return False # Prints an error and returns false if there is a duplicate to allow the user to enter another input

    return True # The program will continue as usual if there is no duplicate found

# --// Main Code \\--
    
createGrid() # Initiating the first procedure to create the grid

while flag == True: # Allowing the loop to continuously run as it is set to true once the grid is created
    displayGrid() # Running the procedure to print out the grid to show updates on every loop
    if all(all(num != 0 for num in row) for row in sGrid):  # Checking to see if the user has completed the sudoku grid
        print("Well done, the sudoku grid has been completed!") # Outputing the results that the grid has been completed.
        break # Breaking the loop to end the program as the game is over.
    else: # If the grid is not complete then the code below will run
        row, column, num = map(int, input("Enter row, column, number where 0 is the first row & column (0-8 | 0-8 | 1-9): ").split()) # Entering the numbers and passing it into the procedure as a paramater to append it to the grid
        if 0 <= row < 9 and 0 <= column < 9 and 1 <= num <= 9 and validateMove(row, column, num): # Checking that the users input is a valid move before appending it to the grid
            sGrid[row][column] = num # If the number is validated and accurate the number will be placed in the row and column given
        else: # if the data entered is not validated it will run the code below
            print("ERROR - Invalid move, try again. Please make sure you did not \n Add duplicates \n Enter 0 for the number \n Enter a number higher than 9 \n Enter a number in a full row \n Enter a number in a full column") # Outputting to the user that there is an error and they msut re-enter a number
            time.sleep(3)
flag == False # Once the game has finished the flag is set to False to break the loop and prevent it from running.