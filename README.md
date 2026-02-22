# Pixel Character Designer
Video Demo: https://youtu.be/g_Uj-CJWlCM

#### Create your own pixel character!!

## Credits
### Libraries:
- pygame
- pygame widgets
### Assets:
- Font: https://online-fonts.com/fonts/determination
### Programs:
- Visual Studio Code
- Aseprite

## How to Play
1. Run main.py.
2. Select the features of your choice and their colour.
3. Once done, press the "Save" button. The image of your character should be saved in the project folder.
4. Quit the game by pressing the X on the top right corner.

## Creation Process
### Idea
I have prior experience making simple games with javascript and on the game engine Godot. I was working on a game on Godot and wanted to make a character creation menu (as every good game has). I decided to implement a simple character designer for my final project of CS50P. I already made a few pixel characters using Aseprite, and borrowed the "base" of the character and some of their features from there.

I decided to use the pygame library as its the most popular for making visual games on python. I also installed the pygame widgets library that uses pygame to provide widgets like buttons and textboxes. I coded on Visual Studio Code, and used Aseprite to draw the pixel sprites.

### Code Structure
project: Contains the main pygame loop that draws the buttons, textbox and handles drawing the features that are selected. It imports data from the other scripts.

Scripts Folder:
  - buttonFunc: Loads the buttons images. Holds the functions for creating the different types of buttons.
  - character: Loads the character and feature images. Holds the data of each feature as a dictionary of lists.
  - coloring: Generates the list of colours. Has the function for changing colours of an image.
  - extras: Has old code that I probably don't need anymore.

Assets Folder:
  - Downloaded fonts
  - Aseprite files I used to draw the sprites
  - Button images folder has the images for the buttons of their inactive, hover and pressed states.
  - Character images folder has the images of all the styles for each feature.

## Further Updates
1.1:
  - Classes
  - Flip button (to flip the styles horizontally)

1.2:
  - Main Screen
  - Credits Page
  - Quit Button

1.3:
  - Sprites for other sides (left, right, back)
  - Pages for more styles