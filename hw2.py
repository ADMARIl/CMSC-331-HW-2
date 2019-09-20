# File: hw2.py
# Project; CMSC 331 HW2
# Author: Andrew Ingson (aings1@umbc.edu)
# Date: 9/30/2018
# Program to read a data file, calculate, and return the statistics

# constants
DATE = 0
MATCH = 1
SHOT_DISTANCE = 2
PLAYER = 3
RESULT = 4

LINE_LENGTH = 5
# CHANGE THIS CONSTANT TO DESIRED DATA CSV FILE
FILE = "test-data.csv"

# function loads date from a give file into a 2D array of data
# returns a 2D array of file data
def loadData(filename):
    # load all file characters into an array we can understand
    fileObj = open(filename)
    lines = fileObj.readlines()
    fileObj.close()

    # create temp vars for our data and possible errors
    resultList = []
    errorInfo = []
    index = 1
    iErrors = 0;
    vErrors = 0;

    # loop to put each line in its own array
    while index < len(lines):
        # try block to catch any excpetions
        try:
            # print(index+1),
            # split string from file based on where commas are
            line = lines[index].strip().split(",")

            # if it's too short, raise an error
            if len(line) < LINE_LENGTH:
                raise IndexError

            # convert strings to neccessary types
            line[SHOT_DISTANCE] = float(line[SHOT_DISTANCE])
            line[RESULT] = int(line[RESULT])

            # append line array to data array
            resultList.append(line)
            index += 1

        # handle index errors by counting them and advancing index
        except IndexError:
            # print("iError")
            iErrors += 1
            index += 1

        # handle value errors by counting them and advancing the index
        except ValueError:
            # print("vError")
            vErrors += 1
            index += 1

        # catch any other possible errors and then advance the index
        except:
            print("Other Error")
            index += 1

    # add error data to error array
    errorInfo.append(index-1)
    errorInfo.append(iErrors)
    errorInfo.append(vErrors)

    # append error array to data array so we can look at it later
    resultList.append(errorInfo)

    # return now full array
    return resultList

# test function to print data Array contents
def printData(data):
    # iterate through all spots in array
    count = 0
    for i in data:
        print count,
        print(i)
        count += 1

# generates statistics given a 2D array of data
def generateStats(data):
    # print total num of records first since that's easy
    print("Total number of records:"),
    print(data[len(data)-1][0])

    # pull error data from end of array
    indexErrors = data[len(data)-1][1]
    valueErrors = data[len(data)-1][2]

    # delete the error array since we dont need it anymore 
    del data[len(data)-1]

    # remember any zero errors
    zeroErrors = 0

    # try catch block for zero errors
    try:
        # vars to store data for statistic math
        numRecords = 0
        totalResults = 0
        totalDistance = 0

        # loop to iterate through all verified data
        for i in range(0,len(data)):
            # another check to make sure it isnt messy
            if (isinstance(data[i][SHOT_DISTANCE], float) == True) and (isinstance(data[i][RESULT], int) == True):
                # if the shot was succesfull, record it and add its data to the vars
                if data[i][RESULT] == 1: 
                    numRecords += 1;
                    totalResults += data[i][RESULT]
                    totalDistance += data[i][SHOT_DISTANCE]

            else:
                # just incase we check value again
                valueErrors += 1
        
        # calculate final result
        result = totalDistance/totalResults * 1.0

    # handle zero errors by increasing the error count and seting the result -1
    except:
        zeroErrors += 1
        result = -1

    # print all of the stats we've gathered
    print("The number of records used for calculation:"),
    print(numRecords)
    print("The average successful shot distance:"),
    # round result to 2 decimal places
    print(round(result,2))
    print("Number of index errors:"),
    print(indexErrors)
    print("Number of value errors:"),
    print(valueErrors)
    print("Number of division by zero errors:"),
    print(zeroErrors)

# main function to run rest of program
def main():
    # load data from file and generate stats
    data = loadData(FILE)
    generateStats(data)

# call to main to actually run the whole thing
main()
