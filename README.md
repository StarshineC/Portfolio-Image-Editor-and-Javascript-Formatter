# Image Editor

Created for the [Jonathan Renan Esponilla Portfolio Site](https://starshinec.github.io).

This set of programs is what I use to resize images and prepares information to be used on my portfolio website. It resizes each image into a viewing size of a maximum width or height of 1500px and into thumbnail sizes with a maximum width or height of 300px. It also generates a javascript file usable by the portfolio site which holds information on each entry of the portfolio.

## Directory Content

* **baseImages**: A directory holding the raw images that need to be resized.
* **finishedImages**: A non-functional directory I placed here just to hold base images I've already resized.
* **resizedImages**: A directory that *imageEditor.py* saves all it's edited files to. This directory is also read by thumbnailGenerator.py to generate thumbnails (smaller sized images)
* **thumbnails**: A directory that *thumbnailGenerator.py* saves its thumbnails to.

* **imageEditor.py**: Uses information from *portfolioContent.csv* to take images from *baseImages* and resizes them for web use into *resizedImages*.
* **thumbnailGenerator.py**: Resizes the images from *resizedImages* into *thumbnails*. This is a seperate program so I can manually reorder files by name in *resizedImages* first.
* **javascriptGenerator.py**: Uses information from *portfolioContent.csv* to generate *portfolioEntries.js*, a javascript file holding a dictionary with all the portfolio entries.

## portfolioContent.csv

This file contains information for each entry in the portfolio. I use Notion to generate this file. Here is each column that I use. Italicized names are not used in *portfolioContent.csv*.

* **projectTitle**: The title visible in the portfolio site.
* **fileName**: The substring used in file names
* **format**: The format of the project. Falls under "Illustration", "Video", and "Programming Project"
* ***sortedDateInput**: The date that I have to input for sorting purposes.
* **sortedDate**: The sorted date in the form of an 8 digit number.
* ***displayDateInput**: The date that is actually displayed in the website.
* **displayDate**: This holds the manually inserted display date or (if there is no manual display date) the real date in "{Month (Words)} {Day}, {Year}" format.
* ***description**: The description I input and can actually read.
* **readableDescription**: Apparently the functions that convert *portfolioContent.csv* doesn't accept certain characters. This replaces characters like " and \n to be readable by the program and manually replaced by me in *portfolioEntries.js*.
* **url**: If available, a url to the project will appear in the form of a button on the website. If the format is "Video," a youtube embed will instead be available.

## How to Use

1. **Ready the files**
Have the images you want to resize in the ***baseImages* folder and the information file *portfolioContent.csv*.
2. **Run "python imageEditor.py" in the command terminal**
This resizes the base images and saves them to *resizedImages*. During the resizing process a preview of each image will open, and the terminal will print out a number next to the available file names. Enter the matching number to assign the file to the correct file name.
3. **(Optional) Move base images to finishedImages**
This step is done so that in future uses you don't resize the same images.
4. **(Optional) Rename the files in resizedImages**
This step is necessary for when I want a defined main image for each portfolio entry. Each file is named with the format *portfolio-{format}-{fileName}-{number}.webp*, so it's only a matter of swapping the {number}s.
5. **Run "python thumbnailGenerator.py" in the command terminal**
This resizes the already resized images into smaller thumbnails.
6. **Run "python javascriptGenerator.py" in the command terminal**
This generates a javascript file that soley holds a dictionary holding information on each portfolio entry.

If you need to add more files in the future, you won't need to resize all the images previously resized. In the case that images are added to portfolio entries with established files, imageEditor.py takes into account the files already in the *resizedImages* directory. *thumbnailGenerator.py* will override all the files.
