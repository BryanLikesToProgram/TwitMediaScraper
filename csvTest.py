"""
Excel file must be opened, then saved as utf8 .csv, renamed "agileOld.csv"
delimiter:        , 	  Field separator (one character)
lineterminator:	  \r\n 	  String used by writer to terminate a line
quotechar:	  " 	  String to surround fields containing special values (one character)
skipinitialspace: False   Ignore whitespace after the field delimiter
"""
import os
import csv
print (os.getcwd())
    #prints working directory, where file i/o will occur
    #os.chdir(path)
lineNumber = 0
"""
should use "with" command when opening files, stops close, leak errors, but we rebels
with open ('agileOld.csv', newline='', encoding='utf8') as csvfile:
"""
with open('twitData.csv', newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in csvreader:
        #row is an instance of an array, each element of said array is a column
        uniqID = 0
        twitHandle = 10
        mediaCol = 20
        if lineNumber == 0:
            #uncessisary for test, but important for applications as row 0 is titles only 
            print(row[uniqID])
            print(row[twitHandle])
            print(row[mediaCol])
        else: 
            print(row[uniqID])
            print(row[twitHandle])
            print(row[mediaCol])
        print("")
            #seperate row data by newline
        lineNumber = lineNumber + 1  

