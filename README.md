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

### Struggles
The parts I struggled with the most were related to the classes I imported from pygame widgets. I was frustrated because the buttons were drawn over everything else, including the preview images of the styles which i wanted to be on the top. I tried many things like changing the order of drawing surfaces and messing around with the code in the button class of pygame widgets. Eventually, I solved the issue by removing the code that draws the rects for the button in the button class, essentially making the buttons transparent.

I realized that although using libraries is convenient, it's difficult when I need to change their functionality because I don't understand all the methods.

## Further Updates
One thing I could have done better was to use Object Oriented Programming more efficiently. I only used premade objects from pygame such as Surface and Rect, and the Button and TextBox objects from pygame widgets. Although I had different "types" of buttons in the buttonFunc script, they were made by changing the arguments for the Button class (from pygame widgets). When I update the game further, I'll code subclasses of the Button class.

I also want to host this game on web, and I tried to do it on GitHub but apparently it only work for static pages?? Which is odd because I hosted my old javascript games here (I don't remember how I did that) and they still work. I attempted to use pygbag but I couldn't figure it out.

I had way more planned for this project, but I realized they'll take way more than a week to program all those. In my initial concept, I planned to have more styles to choose from and be able to view the character from the left, right and back sides as well. But creating assets for those would be time-consuming, so I decided to forego those features for the base version of the game.

Here are the updates I planned:

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

I managed to complete the course and final project during the winter vacation (with a week to spare) but I'll get busy with university soon. I will slowly work on the updates when I have time.
