# LabsAssesment - Lab 5 Soduku 

### Lab Location
* LabAssessment > Soduku > Lab5.py

### Lab Overview
* In this project I have created the Soduku game. You are able to input your own numbers in the order of row, column, number and this will allow you to input your own values to attempt to beat the game. I will now list the different functions and what they do.
1. createGrid() - Function runs to the code to build the sudoko grid.
2. displayGrid() - Prints out the grid created above to the user.
3. validateMove() - Checks that your input is valid and can be placed in the grid or not
4. Everything under --// Main Code \-- is the whole program that runs which the user will see on the user interface.

### How to download the repository and run the program
1. Download Visual Studio Code or an IDE of your choice. (Visual Studio code it recomended as you can easilly open a GitHub repository.)
2. Log in / Sign up to GitHub (https://github.com/login)
3. Open up the repository, copy the link and then open it with visual studio code by doing the following:
    1. Open Source Control > Clone Github Repository
    2. Paste the link in the top menu which opens up
    3. Select the link you've pasted
    4. Click enter and then wait, it will load up shortly after you have followed these steps.
    5. You will then be able to view the 3 labs projects which have been uploaded. You will then get access to the README.md files, Source code and the user interfance once you have ran the code.

### How to use the Sudoku game.
Firstly, once you have accessed the code click F5 or Run > Run with Debugging and then the user interface will show and it is highly user friendly and easy to operate. It will start off with printing out the grid and then will ask you to input values in the order of row, column, number for example: 0 0 1 will enter the number 1 into the first column in the first row. The code will then run a validation to check to make sure that your number isnt a duplicate, it will also then check if the row and column is full or not. Once it has placed your number the program will loop and re ask you to enter another number to be put in a different position. Once you have entered your number it will re print out the grid to show where the location of where your number has been inputted. If there is an error, the program will then inform the user of all possible mistakes which they have made. The program does not stop until the sudoko grid has been completed, on completeion the code will output a message congratulating the user on finishing the grid. The program will then end and it can be restared by clicking F5 again.