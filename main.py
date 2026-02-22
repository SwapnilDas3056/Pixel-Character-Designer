# Import libraries
import pygame as pg
pg.font.init()
import pygame_widgets as pw
from pygame_widgets.textbox import TextBox

from scripts import buttonFunc as bF
from scripts import character as ch
from scripts import coloring as clr

delta_time = 0.1

# Declare global variables
# charDir = 0
bF.feature = 0
bF.style = [0]*12
bF.colList = [0]*12

global charName
charName = "Chara"

global fDict
fDict = ch.featureDict

gameFont = bF.gameFontPath
font_nameText = pg.font.Font(gameFont, size=26)
font_styleText = pg.font.Font(gameFont, size=30)

nameText = font_nameText.render("Name:", False, "black")
featureTextList = [font_styleText.render(featureName.replace("\n", " "), False, "black") for featureName in fDict["Feature Name"]]

def main():
    # pygame setup
    pg.init()
    global screen
    screen = pg.display.set_mode((900, 720))
    clock = pg.time.Clock()
    running = True
    
    nameBox = TextBox(screen, 320, 5, 260, 35, colour="snow", textColour="black", placeholderTextColour="snow4", fontSize=22, borderColour="skyblue4", radius=10, onSubmit=lambda: change_name(nameBox), placeholderText = " type name")

    while running:
        screen.fill("skyblue2")

        # Poll for events
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                running = False

        ## Name text
        screen.blit(nameText, (235,5))
        if len(nameBox.getText()) > 12:
            nameBox.setText(nameBox.getText()[0:12])
            print("Maximum character limit reached")
            nameBox.disable()
        nameBox.enable()

        saveButton = bF.create_smallButton(screen, 800, 5, "Save", onClickFunc=saveChara)

        # Feature Buttons
        buttonList_left = bF.draw_featureButtonsArray(screen, (3,2), (15,85), (150,85), 0, fDict["Feature Name"][:6])
        buttonList_right = bF.draw_featureButtonsArray(screen, (3,2), (610,85), (150,85), 6, fDict["Feature Name"][6:])
        
        if 0 <= bF.feature <= 5:
            buttonList_left[bF.feature].setPressed()
            featureText = featureTextList[bF.feature]
        else:
            buttonList_right[bF.feature-6].setPressed()
            featureText = featureTextList[bF.feature]
        screen.blit(featureText, (40,375))

        global styleList
        styleList = []
        colBox_styles = []

        if not bF.feature == 0:
            previewImgList = [pg.transform.scale(fDict["Style Images"][bF.feature].subsurface(pg.Rect(ch.returnCrop(n),(144,240))), (72,120)) for n in range(12)]

        if bF.feature == 0:
            colBox_skins = bF.draw_colorBoxArray(screen, (6,4), (150,400), (100,80), 0, colorList=clr.colList_skins, scaled=False)
            colBox_skins[bF.colList[0]].setPressed()
            for box in styleList:
                box.hide()
            for box in colBox_styles:
                box.hide()
        else:
            styleList = bF.draw_styleBoxArray(screen, fDict["Style Array Shape"][bF.feature], (40,430), (100,95), bF.feature, 0, imageList=previewImgList, long=fDict["Style Box Long"][bF.feature])
            styleList[bF.style[bF.feature]].setPressed()

            colBox_styles = bF.draw_colorBoxArray(screen, (6,5), (475,380), (70,65), bF.feature, colorList=clr.colList_styles, scaled=True)
            colBox_styles[bF.colList[bF.feature]].setPressed()

            for box in colBox_skins:
                box.hide()
        
        # Seperator bars
        pg.draw.rect(screen, "skyblue4", (0, 350, 900, 11))
        if not bF.feature == 0:
            pg.draw.rect(screen, "skyblue4", (450, 355, 11, 364))

        # Character showing screen
        create_Filledrect(screen, "white", "skyblue4", (325, 50, 250, 280), 3, 10)

        # Character sprites
        draw_feature(1)
        
        baseImage = ch.base_front_img
        baseImage = clr.palette_swap(baseImage, pg.Color(clr.colList_skins[bF.colList[0]]), mode="white")
        screen.blit(baseImage, (375, 70))

        for stI in [3,2,4,5,6,7,10,11,8,9]:
            draw_feature(stI)

        # Update the display on screen
        pw.update(events)
        pg.display.flip()

        delta_time = clock.tick(60) * 0.001
        delta_time = max(0.001, min(0.1, delta_time))

    pg.quit()

def create_Filledrect(surface, fillColor, outlineColor, rect, width=0, border_radius=0):
    pg.draw.rect(surface, fillColor, rect, 0, border_radius)
    pg.draw.rect(surface, outlineColor, rect, width, border_radius)

def change_name(textBox):
    global charName
    charName = textBox.getText()
    print("Name entered:", charName)
    return charName

def draw_feature(stI):
    global screen
    styleImg = fDict["Style Images"][stI]
    styleImg = clr.palette_swap(styleImg, pg.Color(clr.colList_styles[bF.colList[stI]]), mode=fDict["Color Mode"][stI-1])
    screen.blit(styleImg, (375, 70), pg.Rect(ch.returnCrop(bF.style[stI]),(144,240)))

def saveChara():
    global screen
    character = screen.subsurface(pg.Rect((375,70),(144,240)))
    charImg = pg.transform.scale(character, (576, 960))
    global charName
    pg.image.save(charImg, charName+".png")

if __name__ == "__main__":
    main()