# -- Vairables & Services \\--

sGrid = []

# --// Procedures Functions & Paramaters

def createGrid():
    for i in range(9):
        row = []
        for x in range(9):
            row.append(0)
        sGrid.append(row)
    for row in sGrid:
        print(row)
        
# --// Main Code \\--

createGrid()



