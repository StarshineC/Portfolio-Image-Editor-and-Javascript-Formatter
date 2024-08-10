import os
import stdio
from PIL import Image

# (Depracated) Collects the first file of each project in the folder.
# I had this function before 
"""
def thumbCollector(folder):
    # Dictionary
    fileCounts = []

    # Checks for the Maximum of each file.
    for file in os.listdir(folder):
        fileSections = file.split("-")
        fileValue = int(fileSections[3].split(".")[0])

        if fileValue == 0:
            fileCounts += [file]

    return fileCounts
"""
    
# Saves the files in list as thumbnails
def renderImages(inFolder, outFolder, list):
    for file in list:
        # Opens Images
        im = Image.open(f'{inFolder}\{file}')

        # Resizes images
        imWidth = im.width
        imHeight = im.height
        scaleFactor = imWidth/300 if imWidth >= imHeight else imHeight/300
        im1 = im.resize((int(imWidth/scaleFactor), int(imHeight/scaleFactor)))

        # Saves the thumbnail and "notifies" the terminal.
        im1.save(f'{outFolder}/thumb{file[slice(9, None, 1)]}')
        stdio.writeln(f'{file} saved!')

        # Closes images
        im1.close()
        im.close()


"""
def main():
    inFolder = 'resizedImages'
    outFolder = 'thumbnails'

    thumbnailEntries = thumbCollector(inFolder)

    renderImages(inFolder, outFolder, thumbnailEntries)

    stdio.writeln('-=-= Done! =-=-')
"""

# -=-=-= Main Function =-=-=-

def main():
    inFolder = 'resizedImages'
    outFolder = 'thumbnails'

    # Gets a list of each file in inFolder
    thumbnailEntries = os.listdir(inFolder)

    # Resizes and saves each images as a thumbnail.
    renderImages(inFolder, outFolder, thumbnailEntries)

    stdio.writeln('-=-= Done! =-=-')


if __name__ == '__main__':
    main()