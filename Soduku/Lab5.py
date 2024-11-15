# --// Sudoku \\--

# --// Variables & Services \\--

import time
sGrid = []  # Initializing the list to store the numbers in for the grid.
flag = True # Setting the flag to False to ensure that the functions run first to create the grid before activating the loop
isDuplicate = False # Another flag to decide if there has been a duplicated number to decide which statement to run

# Creating the grid and filling it with 0s
for i in range(9): # Creating the rows in the list
    row = [0] * 9  # Filling the row with 0s
    sGrid.append(row) # Applying the rows to the list to be appended on user input
    
   # --// Main Code \\-- 
    
while flag == True:  # Allowing the loop to continuously run
    # Printing the grid which was created above
    for row in sGrid: # Searching the list to find all the rows
        print(" ".join(map(str, row))) # Printing the list in a 9x9 format

    # Checking if the user has completed the sudoku grid
    if all(all(num != 0 for num in row) for row in sGrid):
        print("Well done, the sudoku grid has been completed!")  # Outputing the results that the grid has been completed.
        flag = False # Once the game has finished the flag is set to False to break the loop and prevent it from running.
        
    row, column, num = map(int, input("Enter row, column, number (0-8 | 0-8 | 1-9): ").split()) # Entering the numbers and passing it into the procedure as a paramater to append it to the grid

    # Input validation
    if 0 <= row < 9 and 0 <= column < 9 and 1 <= num <= 9: # Checking that the users input is a valid move before appending it to the grid
        if num in sGrid[row]:  # Checking row for duplicates
            print("ERROR - You cannot have the same number twice in the same row.") # Alerting the user that they cannot enter the same number in the same row 
            continue  # Skip to the next iteration to continue the validation process

        if num in [sGrid[r][column] for r in range(9)]:  # Checking column for duplicates
            print("ERROR - You cannot have the same number twice in a column") # Alerting the user that they cannot enter the same number in the same column
            continue  # Skip to the next iteration to continue the validation process

        # Checking the 3x3 box for duplicates 
        startRow, startColumn = 3 * (row // 3), 3 * (column // 3) # Setting up how the user inputs the data by row, column, number
        for i in range(startRow, startRow + 3): # Checking the grid 3x3 to check for the duplicates
            for j in range(startColumn, startColumn + 3):
                if sGrid[i][j] == num: # Checking the user input for duplicates
                    isDuplicate = True # If a duplicate is found it will make this vairable true to run the correct branch to allert the user of a duplication error.
            if isDuplicate == True: # Checking if the program has registered a duplication error
                print("ERROR - Duplicate found") # Alerting the user that a duplication has ben found and ending the loop for it to be recalled at the top to restart the question
                flag == False # Setting the flag to False to to end the loop and restart the program because of the duplicate.
                

        if isDuplicate == False: # Checking if a program has not registered a duplication error
            sGrid[row][column] = num  # If the number is validated and accurate the number will be placed in the row and column given
        else:
            print("ERROR - Invalid move, try again.") # Outputting to the user that there is an error and they msut re-enter a number
            time.sleep(3)  # Pauses the program to allow the user to read before it resumes, in this case after 3 seconds
    else:
        print("ERROR - Invalid input, try again.") # Outputting to the user that there is an error and they msut re-enter a number
        time.sleep(3)  # Pauses the program to allow the user to read before it resumes, in this case after 3 seconds
flag == False # Once the game has finished the flag is set to False to break the loop and prevent it from running.


        
    