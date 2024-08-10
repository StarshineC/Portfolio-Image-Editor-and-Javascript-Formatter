import os
import stdio
import sys
import csv


# -=-=-= Functions =-=-=-

def makeDictionary(file, outDirectory):
    csvFile = open(file, 'r')
    dict_reader = csv.DictReader(csvFile)

    portfolioEntries = list(dict_reader)

    csvFile.close()

    fileCheck = fileCounter(outDirectory)
    for project in portfolioEntries:
        project["fileCount"] = 0
        if project["fileName"] in fileCheck:
            project["fileCount"] = fileCheck[project["fileName"]]
            
    return portfolioEntries

# Writes to a Javascript File
def makeJavascript(portfolioEntries, outputName):
    fileCheck = os.listdir()
    javascriptPortfolio = open(outputName, "w")
    javascriptPortfolio.write("// -=-=-= Portfolio Entries =-=-=-")
    javascriptPortfolio.close()

    javascriptPortfolio = open(outputName, "a")
    javascriptPortfolio.write("\n\nlet portfolioEntries = [\n")

    entryCurrent = 0;
    entryCount = len(portfolioEntries)

    for entry in portfolioEntries:
        entryCurrent += 1
        
        javascriptPortfolio.write("\t{\n")
        javascriptPortfolio.write(f"\t\ttitle: '{entry['ï»¿projectTitle']}',\n") # title
        javascriptPortfolio.write(f"\t\tfileName: '{entry['fileName']}',\n") # fileName
        javascriptPortfolio.write(f"\t\tfileCount: {entry['fileCount']},\n") # fileCount
        javascriptPortfolio.write(f"\t\tformat: '{entry['format']}',\n") # format
        javascriptPortfolio.write(f"\t\tsortedDate: '{entry['sortedDate']}',\n") # sortedDate
        javascriptPortfolio.write(f"\t\tdisplayDate: '{entry['displayDate']}',\n") # displayDate
        javascriptPortfolio.write(f"\t\turl: '{entry['url']}',\n") # url
        javascriptPortfolio.write(f"\t\tdescription: '{entry['readableDescription']}',\n") # description
        javascriptPortfolio.write("\t},\n" if entryCurrent != entryCount else "\t}\n")

    javascriptPortfolio.write("]")
    
    javascriptPortfolio.close()

# Counts amounts of each file type.
def fileCounter(folder):
    # Dictionary
    fileCounts = {}

    # Checks for the Maximum of each file.
    for file in os.listdir(folder):
        fileSections = file.split("-")
        fileValue = int(fileSections[3].split(".")[0])

        if fileSections[2] in fileCounts and fileValue >= fileCounts[fileSections[2]]:
            fileCounts[fileSections[2]] = fileValue + 1;
        else:
            fileCounts[fileSections[2]] = fileValue + 1;

    return fileCounts



# -=-=-= Main =-=-=-

def main():
    # Creates a dictionary for information on each entry, including the amount of image files each entry has.
    dictionary = makeDictionary("portfolioContent.csv", "resizedImages")
    # Reformats said dictionary into javascript dictionary format.
    makeJavascript(dictionary, "portfolioEntries.js")
    # Completion message.
    stdio.writeln("-=-= Done! =-=-")

if __name__ == '__main__':
    main()