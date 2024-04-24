import csv

grid = []
top = 733940
left = 7603950

for row in range(330):
    grid.append([])
    for column in range(389):
        grid[row].append(0) 

def coordinates():
	count = 0
	with open('Data.csv', 'r') as file:
		readerFile = csv.reader(file)
		for row in readerFile:
			xcoordinate = eval((row[1]))
			ycoordinate = eval((row[2]))
		
			x = int((top - ycoordinate) / 250)
			y = int((xcoordinate - left) / 250)

			try: 
				grid[x][y] +=  1
			except IndexError:
				count += 1  
				
def printBoard(A):
    resultFile = open('Result.txt', 'w')
    for row in grid:
    	for col in row:
    		resultFile.write(str(col))
    	resultFile.write('\n')
    resultFile.close()

coordinates()
printBoard(grid)