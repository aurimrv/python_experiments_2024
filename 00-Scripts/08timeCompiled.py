#!/usr/bin/env python3

# Script that merges all time data into a single spreadsheet
# Each column of the new file represents a combination of pynguin algorithms


import sys

def main():
    if len(sys.argv) < 2:
        print("error: timeCompiled.py <project root dir> <test-sets file name> <mutation-tool-file>")
        print("Example: timeCompiled.py /path test-sets.txt mutation-tools.txt")
        sys.exit(1)

    baseDir = sys.argv[1]
    testSets = sys.argv[2]
    mutToolFile = sys.argv[3]
    mutToolList = baseDir+"/"+mutToolFile

    dadosMutTool = open(mutToolList, 'r')

    for mutTool in dadosMutTool:
        mutTool = mutTool.strip()
        print("Processing mutation tool: ", mutTool)
        prjReport = baseDir+"/compiled-time-report-"+mutTool+".csv"
    
        testSetsFileName = baseDir+"/"+testSets

        # Creates an empty list to store the data from each file
        summaryData = {}

        testSetCount = 1
        with open(testSetsFileName) as testSetsFile:
            for testSet in testSetsFile:
                testSet = testSet.strip()
                reportFileName = baseDir+"/time-report-"+mutTool+"-"+testSet+".csv"
                lineCount = 0;
                with open(reportFileName) as reportFile:
                    for line in reportFile:
                        if (lineCount == 0):
                            lineCount = lineCount + 1
                        else:
                            data = line.split(";")
                            if (testSetCount == 1):
                                summaryData[data[0]] = []
                                #summaryData[data[0]].append(data[1])
                            summaryData[data[0]].append(data[2])
                    testSetCount = testSetCount + 1
            
        with open(prjReport,'w') as outputFile:
            outputFile.write("1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16\n") # Excluding project information from output
            for key in summaryData.keys():
                #outputFile.write(key)
                #outputFile.write(";")
                outputFile.write(';'.join(map(str, summaryData[key])))
                outputFile.write("\n")
    dadosMutTool.close()

if __name__ == "__main__":
    main()
