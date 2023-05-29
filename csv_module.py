import csv
import os
# from operator import is_not

# print(os.getcwd())
csvFile = open(r'C:\Users\csv_files\roster.csv')

#  To open a csv with a "," delimiter
with open(r'C:\Users\csv_files\roster.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',') # Can use without the delimiter argument
    
    # To remove the field name use the next function. First row
    next(csvReader)
    for row in csvReader:
        print(row)
        print(row[3])

#  To open a csv with a Tab "\t" delimiter
with open(r'C:\Users\csv_files\csvRoster.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile, delimiter='\t') # without the delimiter args default to ','
    for row in csvReader:
        print(row)

#  Open a csv as a read only file and create another copy as csvRoster.csv
with open(r'C:\Users\csv_files\roster.csv', 'r') as csvFile:
    csvReader = csv.reader(csvFile)
    #  Create a csv to be written. Writing the data from roster.csv to csvRoster.csv
    with open(r'C:\Users\csv_files\csvRoster.csv', 'w') as newCsvFile:
        csvWriter = csv.writer(newCsvFile, delimiter='\t')
        # csvWriter = csv.writer(newCsvFile)
        for row in csvReader:
            csvWriter.writerow(row)


# Open a csv and create a csvRosterDict.cs as a dictionary.
with open(r'C:\Users\csv_files\roster.csv', 'r') as csvFile:
    csvReaderDict = csv.DictReader(csvFile) # Create a csvReaderDictionary object
    print(csvReaderDict)
    for _dict in csvReaderDict:
        print (_dict,'\n')

    # Create the csvRosterDict.csv
    with open('csvRosterDict.csv', 'w') as newCsvFile:
    #     # Create the header names
        fieldnames = ['No.', 'Player', 'Pos', 'PF', 'Ht', 'Wt','Birth Date', 'Country', 'Exp', 'College']

        # csvWriterDict = csv.DictWriter(newCsvFile, fieldnames=fieldnames)
        csvWriterDict = csv.DictWriter(newCsvFile, fieldnames=fieldnames, delimiter='\t')

        csvWriterDict.writeheader()
        # print(csvWriterDict)# Not iterable
    
        for row in csvReaderDict:
        #     del row['']
            csvWriterDict.writerow(row)
        

roster = []

with open('csvRosterDict.csv', 'r') as rosterCsv:
    csvData = csv.reader(rosterCsv, delimiter='\t')
    # print(csvData)
    for row in csvData:
        if row == []:
            pass
        else:
            # print(row)
            roster.append(row)

for i in roster:
    print(i)

        




