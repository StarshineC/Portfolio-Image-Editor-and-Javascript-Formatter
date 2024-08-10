
# -=-=-= +=+= Mass Image Editor for my Portfolio =+=+ =-=-=-


# Imports

import os
import stdio
import sys
import csv
from PIL import Image



# -=-=-= Functions =-=-=-

# Counts amounts of each file type. (In case there are already images)
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


# Makes Dictionary
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
        

# Resizes Image (Also Renames)
def resize(folderInput, folderOutput, portfolioCandidates):
    baseFiles = os.listdir(folderInput)

    # Goes through all images
    for baseImage in baseFiles:
        # Opens Image
        im = Image.open(f'{folderInput}\{baseImage}')

        # Resizes images
        imWidth = im.width
        imHeight = im.height
        scaleFactor = imWidth/1500 if imWidth >= imHeight else imHeight/1500

        im1 = im.resize((int(imWidth/scaleFactor), int(imHeight/scaleFactor)))

        # Shows and Renames images
        im1.show()
        while True:
            # Prompt
            stdio.writeln("0 | Skip File")
            for project in range(len(portfolioCandidates)):
                stdio.writeln(f'{project + 1} | {portfolioCandidates[project]["fileName"]}')
            stdio.write("> Select File Name by Value: ")
            input = stdio.readInt()
            
            # Checks for Valid Number
            if (input < 0 or input > len(portfolioCandidates)):
                stdio.writeln("Try again!\n")
                continue

            if (input == 0):
                stdio.writeln("Skipped File!\n")
                break

            im1.save(f'{folderOutput}\portfolio-{portfolioCandidates[input - 1]["format"]}-{portfolioCandidates[input - 1]["fileName"]}-{portfolioCandidates[input - 1]["fileCount"]}.webp')
            portfolioCandidates[input - 1]["fileCount"] += 1
            stdio.writeln()
            break

        # Closes images.
        im.close()
        im1.close()


def writeFilecounts(portfolioEntries):
    dict = []
    for entry in range(len(portfolioEntries)):
        dict.append({})
        dict[entry]['fileName'] = portfolioEntries[entry]["fileName"]
        dict[entry]['count'] = portfolioEntries[entry]["fileCount"]
    with open('fileCounts.csv', 'w') as fileCounter:
        writer = csv.DictWriter(fileCounter, ["fileName", "count"])
        writer.writeheader()
        writer.writerows(dict)



# -=-=-= Main Function =-=-=-

def main():
    file = "portfolioContent.csv" # Originally sys.argv[1]
    folderInput = "baseImages" # Originally sys.argv[2]
    folderOutput = "resizedImages" # Originally sys.argv[3]
    # There was also a sys.argv[4] that toggles if the images were to be resized (This entire thing was originally going to be one program).

    portfolioEntries = makeDictionary(file, folderOutput)

    resize(folderInput, folderOutput, portfolioEntries)
    writeFilecounts(portfolioEntries)

    stdio.writeln("-=-= Done! =-=-\n")


if __name__ == '__main__':
    main()