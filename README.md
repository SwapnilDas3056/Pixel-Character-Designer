# Pixel Character Designer
Video Demo: https://youtu.be/g_Uj-CJWlCM

#### Create your own pixel character!!

## How to Play
1. Run main.py.
2. Select the features of your choice and their colour.
3. Once done, press the "Save" button. The image of your character should be saved in the project folder.
4. Quit the game by pressing the X on the top right corner.

## Creation Process
### Idea

### Struggles
The parts I struggled with the most were related to the classes I imported from pygame widgets. I was frustrated because the buttons were drawn over everything else, including the preview images of the styles which i wanted to be on the top. I tried many things like changing the order of drawing surfaces and messing around with the code in the button class of pygame widgets. Eventually, I solved the issue by removing the code that draws the rects for the button in the button class, essentially making the buttons transparent.

I realized that although using libraries is conveneient, it's difficult when I need to change their functionality because I don't understand all the methods.

## Further Updates
One thing I could have done better was to use Object Oriented Programming more efficiently. I only used premade objects from pygame such as Surface and Rect, and the Button and TextBox objects from pygame widgets. Although I had different "types" of buttons in the buttonFunc script, they were made by changing the arguments for the Button class (from pygame widgets). When I update the game further, I'll code subclasses of the Button class.

I also want to host this game on web, and I tried to do it on GitHub but apparently it only work for static pages?? Which is odd because I hosted my old javascript games here (I don't remember how I did that) and they still work. I attempted to use pygbag but I couldn't figure it out.

I had way more planned for this project, but I realized they'll take way more than a week to program all those. In my initial concept, I planned to have more styles to choose from and be able to view the character from the left, right and back sides as well. But creating assets for those would be time-consuming, so I decided to forego those features for the base version of the game.

These are the updates I planned:

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
