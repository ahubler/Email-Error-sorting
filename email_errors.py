import csv

#setup filename
fname = 'customerio_sample_data.csv'

#myFields will hold fieldnames, and myRows will hold the rows of data
myFields = []
myRows = []

#open the csv file and create a reader object
csvfile = open(fname, 'r')
myReader = csv.reader(csvfile)

#take the forst row of the csv file as row names
fields = myReader.next()

#extract all the rows
for r in myReader: #iterate through the remaining rows in the file
        myRows.append(r) #add each row to the end my Rows

#this dictionary will store the unique errors as keys
#and keep a count of each as the value
myDict = {}

#Runs through all the errors we have sotred in myRows
for e in myRows:
    #puts the status number and the error message together in the same string
    err = e[0] + ': ' + e[1]
    #increases the counter if the error has already been encountered
    if err in myDict: myDict[err] += 1
    #if it's anew error, add it and start the counter
    else: myDict [err] = 1

#Sorts dictionary values in order based on dictionary values(occurances of the error)
#revers = true sorts it in descending order
descDict = sorted(myDict, key=myDict.get, reverse = True)

#prints the ten most common errors
for k in range(0,10):
    print(str(k+1)+') Status:'+str(myDict[descDict[k]])+'\n   Error Message: '+str(descDict[k]))
