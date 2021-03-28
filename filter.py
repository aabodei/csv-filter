# Filtering through tab separated values text file to retrieve Canadian cities with a population >= 40,000
# 2020-12-04

# Import required libraries
import csv
import time

# Define a 2-dimensional list with the wanted arguments
outputList = [['City', 'Latitude', 'Longitude', 'Population']]

fileName = 'CA.txt'
print('File ' + fileName + ' opening for processing..')

# For fun, let's see how fast the read process is. (On my machine: 0.65s)
startTime = time.time()

i = 0

#
# Begin the read process
#
# Open the existing file, and set the parameters so it can be read properly
with open(fileName, newline='', encoding='utf-8') as file:
    fileReader = csv.reader(file, delimiter='	')

	# Iterate through each row in the file
    for row in fileReader:

        # If the row is a city or village (P), and the population is greater or equal to 40000, append  to list
        if row[6] == 'P' and int(row[14]) >= 40000:

        	# [2] = City, [4] = Latitude, [5] = Longitude, [14] = Population
            toAppend = [row[2], row[4], row[5], row[14]]
            outputList.append(toAppend)

            # +1 to our counter for a total number of records recorded
            i += 1

# Get the difference in time from our stored start time and current time
endTime = time.time() - startTime
print('Read operation complete. ' + str(i) + ' records read. Time: (' + str(round(endTime, 2)) + 's)')

#
# Begin the write process
#
newFileName = 'City_Data.csv'

# Create a new .csv file that will contain all our collected data
# 'w' -> open for writing
with open(newFileName, 'w') as newFile:
    fileWriter = csv.writer(newFile, delimiter=',', lineterminator='\n')

	# Iterate through every record in the list to write to the new file
    for out in outputList:
        fileWriter.writerow(out)

print('Write operation to ' + newFileName + ' complete.')