import pygame as pg
import pygame_widgets as pw
from pygame_widgets.button import Button
import os, sys

sys.path.append(os.path.join("scripts"))
from character import resizeList

buttonModeList = ["_inactive.png", "_hover.png", "_press.png"]

button_imgList = [pg.image.load(os.path.join("assets", "images", "button_images", "buttonBox" + modeName)) for modeName in buttonModeList]
styleBox_imgList = [pg.image.load(os.path.join("assets", "images", "button_images", "styleBox" + modeName)) for modeName in buttonModeList]
styleBoxLong_imgList = [pg.image.load(os.path.join("assets", "images", "button_images", "styleBoxLong" + modeName)) for modeName in buttonModeList]
smallColorBox_imgList = [pg.image.load(os.path.join("assets", "images", "button_images", "smallColorBox" + modeName)) for modeName in buttonModeList]
smallButton_imgList = [pg.image.load(os.path.join("assets", "images", "button_images", "smallButton" + modeName)) for modeName in buttonModeList]

gameFontPath = os.path.join("assets", "fonts", "DTM", "DTM-Sans.otf")
font_buttonText = pg.font.Font(gameFontPath, 24)

global feature
feature = 0
global style
style = [0]*12
global colList
colList = [0]*12

def set_feature(ftN) -> None:
    """
    Sets the current feature number to ftN
    
    :param ftN: Number of the feature to set
    :type ftN: int
    """
    global feature
    if not feature == ftN:
        feature = ftN
        # print("Feature selected:", feature)

def set_style(stI, stN) -> None:
    """
    Sets the current style number of style at index stI to stN
    
    :param stI: Index of the style
    :type stI: int
    :param stN: Number of the style to set
    :type stN: int
    """
    global style

    if not style[stI] == stN:
        style[stI] = stN
        # print(f"Style {stI} selected:", style[stI])

def set_color(stI, colN) -> None:
    """
    Sets the current color number of selected style to colN
    
    :param stI: Index of the style
    :type stI: int
    :param stN: Number of the style to set
    :type stN: int
    """
    global colList

    if not colList[stI] == colN:
        colList[stI] = colN
        # print(f"Color {colN} selected for feature {stI}")

def create_featureButton(surface, xPos, yPos, buttonText, ftN=0) -> Button:
    """
    Returns a button that changes the selected feature when clicked
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param xPos: X-coordinate of the top left corner
    :type xPos: int
    :param yPos: Y-coordinate of the top left corner
    :type yPos: int
    :param buttonText: Text of display on button
    :type buttonText: str
    :param ftN: Number of the feature to set
    :type ftN: int
    :return: A py_widget button with the given properties
    :rtype: Button
    """
    buttonArgs = {"font": font_buttonText, "fontSize": 20, "image": button_imgList[0], "onHoverImage": button_imgList[1], "onPressImage": button_imgList[2]}
    button = Button(surface, xPos, yPos, 130, 70, radius=10, text=buttonText, onClick=lambda: set_feature(ftN), **buttonArgs)
    return button

def draw_featureButtonsArray(surface, shape=(2,1), startPos=(0,0), spacing=(10,10), startN=0, bNames=["B0","B1"]) -> list:
    """
    Returns a list of feature buttons arranged in an array
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param shape: Tuple in the form (height, width) of the array
    :type shape: tuple
    :param startPos: Tuple in the form (xPos, yPos) of the top left coordinate of the array
    :type startPos: tuple
    :param spacing: Tuple in the form (spacingX, spacingY) of the spacing between the buttons
    :type spacing: tuple
    :param startN: Number to start the array with (for ftN)
    :type startN: int
    :param bNames: List of names of the buttons
    :type bNames: list
    :return: List of the buttons in the array
    :rtype: list
    """
    buttonList = []
    height, width = shape
    startX, startY = startPos
    spacingX, spacingY = spacing

    for i in range(width):
        for j in range(height):
            btn = create_featureButton(surface, startX+spacingX*i, startY+spacingY*j, bNames[j+i*height], j+i*height+startN)
            buttonList.append(btn)

    return buttonList

def create_styleBox(surface, xPos, yPos, stI=0, stN=0, long=False) -> Button:
    """
    Returns a button that changes the selected style when clicked
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param xPos: X-coordinate of the top left corner
    :type xPos: int
    :param yPos: Y-coordinate of the top left corner
    :type yPos: int
    :param stI: Index of the style to change
    :type stI: int
    :param stN: Number of the style to set
    :type stN: int
    :return: A py_widget button with the given properties
    :rtype: Button
    """
    boxImgList = styleBox_imgList
    if long == True:
        boxImgList = styleBoxLong_imgList
    buttonArgs = {"image": boxImgList[0], "onHoverImage": boxImgList[1], "onPressImage": boxImgList[2]}
    
    button = Button(surface, xPos, yPos, 60, 60, radius=10, onClick=lambda: set_style(stI, stN), **buttonArgs)
    return button

def draw_styleBoxArray(surface, shape=(2,1), startPos=(0,0), spacing=(10,10), stI=0, startN=0, imageList=None, long=False) -> list:
    """
    Returns a list of style boxes arranged in an array
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param shape: Tuple in the form (width, height) of the array
    :type shape: tuple
    :param startPos: Tuple in the form (xPos, yPos) of the top left coordinate of the array
    :type startPos: tuple
    :param spacing: Tuple in the form (spacingX, spacingY) of the spacing between the buttons
    :type spacing: tuple
    :param stI: Index of the style to change
    :type stI: int
    :param startN: Number to start the array with (for stN)
    :type startN: int
    :param imageList: list of images to put on the boxes
    :type imageList: list
    :return: List of the buttons in the array
    :rtype: list
    """
    boxList = []
    width, height = shape
    startX, startY = startPos
    spacingX, spacingY = spacing

    resizeN, xOffset, yOffset = resizeList[stI-1]

    for i in range(height):
        for j in range(width):
            box = create_styleBox(surface, startX+spacingX*j, startY+spacingY*i, stI, j+i*width+startN, long=long)
            if long == True:
                pg.draw.rect(surface, (255,255,255), (startX+spacingX*j, startY+spacingY*i-10, 60,80), border_radius=12)
            else:
                pg.draw.rect(surface, (255,255,255), (startX+spacingX*j, startY+spacingY*i, 60,60), border_radius=10)
            if not stI == 0:
                styleImg = imageList[j+i*4]
                scaledImg = pg.transform.scale(styleImg, (72*resizeN, 120*resizeN))
                surface.blit(scaledImg, (startX+spacingX*j+xOffset, startY+spacingY*i+yOffset))
            boxList.append(box)

    return boxList

def create_colorBox(surface, xPos, yPos, stI=0, colN=0, scaled=False) -> Button:
    """
    Returns a button that changes the selected color of the chosen style when clicked
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param xPos: X-coordinate of the top left corner
    :type xPos: int
    :param yPos: Y-coordinate of the top left corner
    :type yPos: int
    :param stI: Index of the style to change
    :type stI: int
    :param stN: Number of the style to set
    :type stN: int
    :param colN: Color number to set in the form of a tuple
    :type colN: int
    :return: A py_widget button with the given properties
    :rtype: Button
    """
    boxImgList = styleBox_imgList
    if scaled == True:
        boxImgList = smallColorBox_imgList

    buttonArgs = {"image": boxImgList[0], "onHoverImage": boxImgList[1], "onPressImage": boxImgList[2]}
    button = Button(surface, xPos, yPos, 60, 60, radius=10, onClick=lambda: set_color(stI, colN), **buttonArgs)
    return button

def draw_colorBoxArray(surface, shape=(2,1), startPos=(0,0), spacing=(10,10), stI=0, colorList=None, scaled=False) -> list:
    """
    Returns a list of color boxes arranged in an array
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param shape: Tuple in the form (width, height) of the array
    :type shape: tuple
    :param startPos: Tuple in the form (xPos, yPos) of the top left coordinate of the array
    :type startPos: tuple
    :param spacing: Tuple in the form (spacingX, spacingY) of the spacing between the buttons
    :type spacing: tuple
    :param stI: Index of the style to change
    :type stI: int
    :param stN: Number of style to change
    :type stN: int
    :param colorList: list of colors to put on the boxes
    :type colorList: list
    :return: List of the buttons in the array
    :rtype: list
    """
    boxList = []
    width, height = shape
    startX, startY = startPos
    spacingX, spacingY = spacing

    for i in range(height):
        for j in range(width):
            box = create_colorBox(surface, startX+spacingX*j, startY+spacingY*i, stI, j+i*width, scaled=scaled)
            color = colorList[j+i*width]
            if scaled == True:
                pg.draw.rect(surface, color, (startX+spacingX*j+8, startY+spacingY*i+8, 45,45), border_radius=30)
            else:
                pg.draw.rect(surface, color, (startX+spacingX*j, startY+spacingY*i, 60,60), border_radius=10)
            boxList.append(box)
    return boxList

def create_smallButton(surface, xPos, yPos, buttonText, onClickFunc=None) -> Button:
    """
    Returns a button that changes the selected feature when clicked
    
    :param surface: Surface to place button on
    :type surface: pygame.Surface
    :param xPos: X-coordinate of the top left corner
    :type xPos: int
    :param yPos: Y-coordinate of the top left corner
    :type yPos: int
    :param buttonText: Text of display on button
    :type buttonText: str
    :param ftN: Number of the feature to set
    :type ftN: int
    :return: A py_widget button with the given properties
    :rtype: Button
    """
    buttonArgs = {"font": font_buttonText, "fontSize": 30, "image": smallButton_imgList[0], "onHoverImage": smallButton_imgList[1], "onPressImage": smallButton_imgList[2]}
    button = Button(surface, xPos, yPos, 70, 70, radius=10, text=buttonText, onClick=onClickFunc, **buttonArgs)
    return button